from app.agent.controller import TaskController
from app.agent.task import TaskState

# Maintain AgentRuntime for compatibility with main.py, but delegate to TaskController
class AgentRuntime:
    def __init__(self):
        self.controller = TaskController()

    def toggle_debug(self, state: bool):
        self.controller.toggle_debug(state)

    def process_input(self, user_input: str) -> tuple[str, str]:
        return self.controller.process_input(user_input)

