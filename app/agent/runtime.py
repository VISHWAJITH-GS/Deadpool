import json
import re
import time
from app.llm.ollama import OllamaClient
from app.agent.planner import PromptBuilder
from app.agent.context import context_manager
from app.tools.registry import tool_registry
from app.agent.persona import Persona
from app.agent.safety import safety_controller
from app.agent.intent_parser import intent_parser
from app.tools.app_discovery import app_discovery
from app.agent.state import StateMachine, AgentState

import app.tools.calculator
import app.tools.system_info
import app.tools.files
import app.tools.web
import app.tools.desktop
import app.observation.ui_tree

class TaskState:
    def __init__(self, goal: str, steps: list):
        self.goal = goal
        self.steps = steps
        self.current_step = 0
        self.active_application = None
        self.active_window = None

class AgentRuntime:
    def __init__(self):
        from app.llm.ollama import OllamaClient
        self.llm = OllamaClient()
        self.tools = tool_registry.get_schemas()
        self.system_prompt = PromptBuilder.build_system_prompt(self.tools)
        self.max_actions_per_task = 12
        self.debug_mode = False
        self.state_machine = StateMachine()

    def toggle_debug(self, state: bool):
        self.debug_mode = state

    def debug_log(self, section: str, message: str):
        if self.debug_mode:
            print(f"\n[{section.upper()}]\n{message}\n")

    def execute_plan(self, task_state: TaskState) -> str:
        self.debug_log("intent", "multi_step")
        
        parsed_str = "\n".join([f"{i+1}. {step['action']}({step.get('app', step.get('text', step.get('url', '')))})" for i, step in enumerate(task_state.steps)])
        self.debug_log("parsed steps", parsed_str)

        results = []
        for step in task_state.steps:
            action = step["action"]
            
            if action == "open_app":
                raw_app = step["app"]
                resolved = app_discovery.resolve_app(raw_app)
                if not resolved or "ambiguous" in resolved:
                    exe_name = raw_app
                    self.debug_log("resolved app", f"Fallback -> {exe_name}")
                else:
                    exe_name = resolved["executable"]
                    self.debug_log("resolved app", f"{resolved['name']} -> {exe_name}")
                    task_state.active_application = resolved['id']
                
                self.debug_log("permission", safety_controller.get_risk_level("launch_application", {"app_name": exe_name}))
                self.debug_log("executing", f"launch_application({exe_name})")
                
                res = tool_registry.execute("launch_application", {"app_name": exe_name})
                time.sleep(1.5)
                self.debug_log("verification", "SUCCESS" if "Success" in res else "FAILED")
                results.append(res)
                
            elif action == "type_text":
                text = step["text"]
                target_app = step.get("target_app")
                
                if target_app:
                    self.debug_log("executing", f"focus_application({target_app})")
                    tool_registry.execute("focus_application", {"app_name": target_app})
                    time.sleep(0.5)
                
                # Active Window Check
                aw_res = tool_registry.execute("get_active_window", {})
                self.debug_log("current window", aw_res)
                
                self.debug_log("permission", safety_controller.get_risk_level("type_text", {"text": text, "app": target_app or task_state.active_application}))
                self.debug_log("executing", f"type_text(\"{text}\")")
                
                res = tool_registry.execute("type_text", {"text": text})
                self.debug_log("verification", "SUCCESS" if "Success" in res else "FAILED")
                results.append(res)
                
            elif action == "open_url":
                url = step["url"]
                self.debug_log("executing", f"open_url({url})")
                res = tool_registry.execute("open_url", {"url": url})
                results.append(res)
                
            elif action == "search":
                query = step["query"]
                self.debug_log("executing", f"web_search({query})")
                res = tool_registry.execute("web_search", {"query": query})
                results.append(res)

        return "\n".join(results)

    def process_input(self, user_input: str) -> tuple[str, str]:
        # Handle fast-path intent parsing
        self.state_machine.transition(AgentState.UNDERSTANDING)
        plan = intent_parser.parse_intent(user_input)
        if plan:
            self.state_machine.transition(AgentState.PLANNING)
            task = TaskState(plan["goal"], plan["steps"])
            self.state_machine.transition(AgentState.EXECUTING)
            results = self.execute_plan(task)
            self.state_machine.transition(AgentState.VERIFYING)
            self.state_machine.transition(AgentState.COMPLETED)
            msg = f"Done. Task executed successfully.\n{results}"
            self.state_machine.transition(AgentState.IDLE)
            return Persona.format_response("Done. " + plan["goal"]), Persona.format_response("Done.")

        self.state_machine.transition(AgentState.OBSERVING)
        # Inject basic observation context before starting the LLM loop to save a tool call
        try:
            active_window = tool_registry.execute("get_active_window", {})
            observation = f"User Request: {user_input}\nCurrent Active Window: {active_window}"
        except Exception:
            observation = user_input
            
        context_manager.add_message("user", observation)
        action_count = 0
        
        while action_count < self.max_actions_per_task:
            self.state_machine.transition(AgentState.PLANNING)
            action_count += 1
            prompt = PromptBuilder.build_user_prompt(user_input)
            
            full_response = ""
            for chunk in self.llm.generate(prompt, system=self.system_prompt, stream=False):
                full_response += chunk
                
            try:
                json_str = full_response
                if "```json" in full_response:
                    json_str = full_response.split("```json")[1].split("```")[0]
                elif "```" in full_response:
                    json_str = full_response.split("```")[1].split("```")[0]
                else:
                    match = re.search(r'(\{.*\})', full_response, re.DOTALL)
                    if match:
                        json_str = match.group(1)
                    else:
                        json_str = full_response.strip()
                        if not json_str.startswith("{") and '"text"' in json_str:
                            json_str = "{" + json_str
                        if not json_str.endswith("}"):
                            json_str = json_str + "}"
                    
                data = json.loads(json_str.strip())
                text = data.get("text", "")
                voice_text = data.get("voice_text", text)
                if not voice_text:
                    voice_text = text
                tool_calls = data.get("tool_calls", [])
                
                if isinstance(tool_calls, dict):
                    tool_calls = [tool_calls]
                
                if not tool_calls:
                    self.state_machine.transition(AgentState.COMPLETED)
                    context_manager.add_message("assistant", text)
                    self.state_machine.transition(AgentState.IDLE)
                    return Persona.format_response(text), Persona.format_response(voice_text)
                    
                print(f"\n[Deadpool is thinking...] {text}")
                
                tool_results = []
                self.state_machine.transition(AgentState.EXECUTING)
                for call in tool_calls:
                    name = call.get("name")
                    args = call.get("arguments", {})
                    
                    risk = safety_controller.get_risk_level(name, args)
                    if risk == safety_controller.DANGEROUS or risk == safety_controller.CONFIRM:
                        self.state_machine.transition(AgentState.WAITING_PERMISSION)
                        print(f"\n⚠️ WARNING: Deadpool wants to execute a {risk} action: {name}({args})")
                        confirm = input("Allow? (y/n): ").strip().lower()
                        if confirm != 'y':
                            print("Action cancelled by user.")
                            tool_results.append(f"Tool '{name}' execution was DENIED by the user for safety.")
                            self.state_machine.transition(AgentState.EXECUTING)
                            continue
                        self.state_machine.transition(AgentState.EXECUTING)
                    
                    print(f"🔧 Executing {name}({args})...")
                    result = tool_registry.execute(name, args)
                    tool_results.append(f"Tool '{name}' returned: {result}")
                
                self.state_machine.transition(AgentState.VERIFYING)
                user_input = "System Info (Tool Results):\n" + "\n".join(tool_results)
                context_manager.add_message("assistant", text + f" (Called: {[c.get('name') for c in tool_calls]})")
                
            except json.JSONDecodeError:
                self.state_machine.transition(AgentState.FAILED)
                msg = "I couldn't form a valid action plan. Let me try again or you can rephrase."
                context_manager.add_message("assistant", msg)
                self.state_machine.transition(AgentState.IDLE)
                return Persona.format_response(msg), Persona.format_response(msg)
                    
        self.state_machine.transition(AgentState.FAILED)
        msg = "I've been thinking for too long and hit my action limit! Let's try something else."
        formatted_response = Persona.format_response(msg)
        self.state_machine.transition(AgentState.IDLE)
        return formatted_response, formatted_response
