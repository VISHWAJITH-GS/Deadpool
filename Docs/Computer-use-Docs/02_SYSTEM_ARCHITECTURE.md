# System Architecture

## Components

```text
app/
├── runtime
├── llm
├── planner
├── observer
├── executor
├── verifier
├── permissions
├── memory
├── tools
└── persona
```

### Runtime
Owns the task lifecycle.

### LLM
Communicates with local Ollama/Qwen.

### Planner
Converts user intent into a minimal action plan.

### Observer
Determines current desktop state.

### Executor
Performs approved actions.

### Verifier
Determines whether the intended state was reached.

### Permissions
Controls what can happen automatically.

### Memory
Stores only useful explicit long-term information.

### Persona
Formats final communication; it does not control execution.

## State machine

```text
IDLE
 |
 v
UNDERSTAND
 |
 v
OBSERVE
 |
 v
PLAN
 |
 v
EXECUTE
 |
 v
VERIFY
 |     \
 |      \ failure
 |       v
 |     RECOVER
 |       |
 +-------+
 |
 v
DONE
```

A task must never remain in an uncontrolled execution loop.

Default maximum recovery attempts: 2.
Default maximum action count per task: 12.
Both should be configurable.
