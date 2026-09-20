# Target Specification System

The user may explicitly specify the target type.

Examples:
- Open Chrome app.
- Open LeetCode website.
- Open my project folder.
- Switch to Chrome app.

Initial types:
- app
- website

Future types:
- file
- folder
- document
- project
- window
- tab
- setting

Canonical representation:

```json
{"action":"open","target":"Chrome","type":"app"}
```

```json
{"action":"navigate","target":"LeetCode","type":"website"}
```

Resolution priority:
1. explicit type
2. user alias
3. cached registry
4. installed-app registry
5. website registry
6. Qwen inference
7. ask user

Explicit specifications should normally avoid an LLM call.
