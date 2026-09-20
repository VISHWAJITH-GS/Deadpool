# System Architecture

```text
USER
  |
CLI / UI
  |
Agent Runtime
  |----------------------|
  v                      v
Context Manager       Tool Router
  |                      |
Prompt Builder        Validator
  |                      |
Ollama                Tool
  |                      |
Qwen3 1.7B              |
  |----------------------|
  |
Final Response
  |
Persona Layer
```

## Runtime loop
input → classify → retrieve minimal context → model → parse tool call if needed → validate → execute → return compact tool result → final model response → persona formatting.

## Core rule
The LLM selects intent/tools. Deterministic application code controls execution. Model text must never directly become executable code.
