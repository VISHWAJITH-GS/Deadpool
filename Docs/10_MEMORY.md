# Memory System

SQLite is sufficient for the lightweight version.

```text
memories
---------
id
key
value
category
created_at
updated_at
```

Store long-term memory only when the user explicitly asks to remember or approves a proposed memory.

Retrieve only relevant memories, typically 3–5 records.

Commands:
- remember X
- what do you remember about X?
- forget X
- forget everything

Do not automatically store sensitive information.
