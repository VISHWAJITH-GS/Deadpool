# Vibecoding Implementation Prompts

Implement sequentially. Do not ask the coding agent to build the entire product in one pass.

## Prompt 1 — Skeleton

Build a minimal Python Windows desktop-agent repository using the documented structure. Add configuration, CLI, logging, tests and an agent state machine. Do not implement arbitrary command execution.

## Prompt 2 — Ollama

Implement a small streaming Ollama client targeting Qwen3 1.7B. Add timeouts, connection errors and response parsing. Keep dependencies minimal.

## Prompt 3 — Deterministic desktop layer

Implement application launch/focus, URL opening, keyboard actions and basic window detection. Use Windows APIs where practical. Add tests and safety limits.

## Prompt 4 — Structured actions

Implement the action schemas and validator. The LLM may request only registered actions.

## Prompt 5 — Observer

Implement active-window detection and accessibility/UI observation. Add screenshot capture as an explicit fallback only.

## Prompt 6 — Agent loop

Implement:
observe → plan → execute → observe → verify → recover/finish.

Add maximum action and retry limits.

## Prompt 7 — Permissions

Implement SAFE, CONFIRM and DANGEROUS policies plus emergency stop.

## Prompt 8 — Memory

Implement SQLite aliases and explicit memories.

## Prompt 9 — Persona

Add concise witty responses after verified task outcomes.

## Prompt 10 — Performance

Instrument all latency components. Reduce model calls and screenshots. Add a deterministic fast path for common requests.

## Prompt 11 — Test suite

Add unit, integration and performance tests.

## Coding-agent rules

- inspect existing files first
- make minimal changes
- don't introduce large frameworks
- don't expose arbitrary shell execution
- run tests after every milestone
- preserve working behavior
- explain every dependency
