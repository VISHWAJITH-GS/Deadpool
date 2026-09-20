# Vibecoding Plan

Implement one milestone at a time.

## Prompt 1 — Skeleton
Create the Python repository using the documented structure. Add configuration, CLI, logging and tests. No tools yet.

## Prompt 2 — Ollama
Implement a minimal streaming Ollama client for Qwen3 1.7B with timeout and connectivity tests.

## Prompt 3 — Agent runtime
Implement structured outputs and the agent loop. No arbitrary execution.

## Prompt 4 — Tools
Implement calculator, time, system_info, file_search and file_read with schemas and tests.

## Prompt 5 — Memory
Implement SQLite explicit remember/forget functionality.

## Prompt 6 — Persona
Implement a separate persona module. Keep tool decisions independent from personality.

## Prompt 7 — Security
Implement permissions, path restrictions, validation and confirmation.

## Prompt 8 — Performance
Measure latency and remove unnecessary calls/context.

## Prompt 9 — Testing
Add golden conversations and integration tests.

Coding-agent constraints:
- inspect first
- make minimal changes
- preserve working behavior
- run tests
- explain changed files
- justify new dependencies
