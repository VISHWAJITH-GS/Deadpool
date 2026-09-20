# Testing Strategy

## Unit
Test prompt construction, schema parsing, tool validation, permissions, memory, path restrictions and persona modes.

## Integration
Test Ollama connectivity, response parsing, tool loop, SQLite and web adapter.

## Golden conversations
Keep cases for:
- casual chat
- calculation
- memory
- file search
- failed tool
- ambiguity
- confirmation
- cancellation

Evaluate structure and factual correctness, not exact wording.

## Performance
Track p50/p95 latency for simple chat, single-tool and multi-step tool tasks.
