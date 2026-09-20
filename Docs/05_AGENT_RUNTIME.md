# Agent Runtime

## State
```text
session_id
mode
recent_messages
current_task
pending_confirmation
```

## Loop
1. Receive input.
2. Detect cancellation.
3. Retrieve only relevant memory.
4. Build compact prompt.
5. Call Qwen.
6. Parse structured output.
7. If tool call: validate, permission-check, execute.
8. Return compact result to model if another response is needed.
9. Render final response.
10. Persist only required state.

## Limits
Default maximum tool iterations: 3.

If the task cannot finish within the limit, stop and explain.

Cancellation must prevent future tool calls unless an already-running tool cannot safely stop.
