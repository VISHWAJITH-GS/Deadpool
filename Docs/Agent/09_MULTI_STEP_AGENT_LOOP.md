# Multi-Step Agent Loop

```text
GOAL
 ↓
UNDERSTAND
 ↓
OBSERVE
 ↓
PLAN NEXT ACTION
 ↓
PERMISSION CHECK
 ↓
EXECUTE
 ↓
OBSERVE
 ↓
VERIFY
 ├── success → next step / DONE
 ├── recoverable → re-plan
 └── failure → stop safely
```

Example:
"Open Chrome, go to LeetCode, find Two Sum."

State:
1. Chrome unknown
2. Chrome running
3. Chrome active
4. URL = leetcode.com
5. LeetCode UI visible
6. Two Sum located
7. Goal verified

When state is uncertain, execute one action and observe again.

Defaults:
- max 12 actions/task
- max 2 recovery attempts
- max 3 planner calls for a simple task
