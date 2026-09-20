# Performance Engineering

## Goals
Fast, predictable and lightweight.

## Rules
1. One model call when no tool is required.
2. Prefer two calls for a normal tool workflow.
3. Maximum 3 tool iterations.
4. Stream output.
5. Keep prompts compact.
6. Cache static configuration.
7. Keep SQLite simple.
8. Avoid embeddings/vector DBs in v1.
9. Avoid unnecessary background processes.
10. Prefer deterministic local tools.

Measure:
- request latency
- model time-to-first-token
- model total latency
- tool latency
- total task latency

Optimize in this order:
prompt size → unnecessary model calls → tool latency → model settings → micro-optimizations.
