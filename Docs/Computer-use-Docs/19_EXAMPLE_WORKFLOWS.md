# Example Workflows

## Workflow A — Browser

User:
"Open Edge and go to LeetCode."

Fast path:
launch/focus Edge → direct URL → verify → finish.

## Workflow B — Project

User:
"Open my TCE Connect project in VS Code."

Memory:
TCE Connect → known project path.

Execution:
launch/focus VS Code → open project path → verify project window.

## Workflow C — Search

User:
"Open Edge and search for Python decorators."

Execution:
open Edge → focus address/search → enter query → verify search page.

Prefer direct browser navigation when appropriate.

## Workflow D — Multi-step

User:
"Open Edge, go to LeetCode, then open my VS Code project."

Execution:
1. Edge + LeetCode
2. verify
3. VS Code + project
4. verify
5. final response

If one step fails, do not silently continue into unrelated actions.

## Workflow E — Confirmation

User:
"Delete this file."

Agent:
"This will permanently delete the file. Proceed?"

No deletion occurs until confirmation.
