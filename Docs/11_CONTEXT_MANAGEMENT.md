# Context Management

Context layers:
1. system rules
2. current mode
3. relevant memory
4. recent conversation
5. current request
6. relevant tool schema

When context grows:
- remove old low-value turns
- summarize only when needed
- preserve current task state
- preserve unresolved questions

Do not send irrelevant conversations, the whole database, every tool schema or huge documents.
