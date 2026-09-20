# Tool System

Every tool has:
- name
- description
- input schema
- permission level
- timeout
- handler

Execution:
```text
model tool call
→ schema validation
→ permission check
→ timeout
→ execute
→ sanitize result
→ model
```

Keep results compact.

Do not expose arbitrary shell commands, unrestricted subprocess execution or arbitrary Python execution to the model in v1.
