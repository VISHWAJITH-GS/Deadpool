# Deadpool Desktop Computer-Use Agent — Master Build Specification

## 1. Product goal

Build a lightweight Windows desktop AI agent that accepts natural-language goals and operates the user's laptop to complete them.

Example:

User: "Open Edge and go to LeetCode."

Expected behavior:
1. Understand the goal.
2. Plan the minimum required actions.
3. Launch or focus Edge.
4. Navigate to LeetCode.
5. Observe the result.
6. Verify success.
7. Stop.
8. Give a concise response.

The agent must optimize for:
- speed
- precision
- low RAM/CPU overhead
- minimal model calls
- deterministic execution
- safe permissions
- recoverability

## 2. Core architecture

```text
                         USER
                           |
                           v
                 +-------------------+
                 | Qwen3 1.7B        |
                 | Intent + Planner  |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 | Agent Runtime     |
                 | Plan -> Act ->    |
                 | Observe -> Verify |
                 +---------+---------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       UI Automation   Screenshot    Keyboard/Mouse
       / Accessibility   fallback       fallback
             |             |             |
             +-------------+-------------+
                           |
                           v
                    Windows Desktop

       Memory + Permissions + Logs + Persona
                    support the runtime
```

## 3. Golden rule

The model decides WHAT should happen.

Application code decides HOW the action is executed.

Never allow raw LLM text to become an executable shell command or unrestricted automation instruction.

## 4. Minimal execution loop

```text
Goal
 ↓
Classify
 ↓
Plan only if necessary
 ↓
Observe current state
 ↓
Choose one action
 ↓
Execute
 ↓
Observe
 ↓
Verify
 ↓
Done / Retry / Re-plan
```

Do not generate a huge plan when a single deterministic action is enough.

## 5. Example

Input:
"Open Edge and go to LeetCode."

Internal task:

```text
Goal:
Navigate browser to LeetCode.

Actions:
1. Find or launch Edge.
2. Focus Edge.
3. Navigate to https://leetcode.com.
4. Verify browser/page state.
```

The user should not need to say:
"click Edge, click address bar, type URL, press Enter."

## 6. Scope for v1

### Must have
- Windows support
- Qwen3 1.7B via Ollama
- text CLI
- application launcher
- window detection/focus
- keyboard actions
- mouse actions
- URL navigation
- screenshot capture
- basic screen/UI observation
- action verification
- retry/re-plan
- permission system
- emergency stop
- logging
- concise persona responses

### Deferred
- full vision-language model
- unrestricted terminal control
- autonomous destructive operations
- continuous screen recording
- multi-agent architecture
- large vector database
- complex GUI framework
- cloud dependency for normal tasks

## 7. Performance philosophy

Prefer deterministic mechanisms over LLM reasoning.

Examples:

"Open Edge" -> application launcher, not vision.

"Go to LeetCode" -> browser address navigation, not clicking a search engine.

"Press Ctrl+S" -> keyboard event, not screen recognition.

Use screenshots/UI analysis only when the state cannot be determined more reliably.
