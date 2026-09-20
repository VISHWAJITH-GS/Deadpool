# Agent Loop

## Fast path

For simple requests:

```text
User
 ↓
Intent detection
 ↓
Known deterministic tool
 ↓
Execute
 ↓
Verify
 ↓
Response
```

Example:
"Open Edge."

No complex planning is necessary.

## General path

```text
User goal
 ↓
Qwen determines task
 ↓
Observer checks current state
 ↓
Planner creates next action
 ↓
Executor performs action
 ↓
Observer checks result
 ↓
Verifier
 ├── success → finish
 ├── recoverable → retry/re-plan
 └── failure → explain
```

## One-action-at-a-time principle

Prefer:

```text
observe → action → observe → action
```

over:

```text
generate 20 actions → execute blindly
```

This makes recovery more reliable.

## Limits

- max 12 actions/task
- max 2 recovery attempts
- max 3 model tool-planning calls for a simple task
- configurable timeouts
- immediate emergency stop
