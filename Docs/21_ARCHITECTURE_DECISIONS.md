# Architecture Decisions

## ADR-001 Local-first LLM
Use Qwen3 1.7B through Ollama for low resource use, privacy and fast iteration.

## ADR-002 Python runtime
Use Python for simple integration with local AI, files, tools and future voice.

## ADR-003 SQLite
Use SQLite instead of a vector database for v1 because explicit memory is small and structured.

## ADR-004 CLI first
Build the terminal interface before GUI for faster feedback and a smaller surface.

## ADR-005 Deterministic tools
Application code executes tools; the model only requests them.

## ADR-006 Personality after execution
Render personality from verified outcomes so humor cannot corrupt action correctness.
