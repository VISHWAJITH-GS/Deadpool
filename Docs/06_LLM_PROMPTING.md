# LLM Prompting Strategy

Qwen3 1.7B benefits from short, relevant prompts.

## Include
- role
- available relevant tools
- output schema
- safety rules
- current mode
- response length
- current time only when relevant

## Avoid
- entire conversation history
- irrelevant memories
- huge documentation
- every tool definition on every request

## Structured output
```json
{"type":"tool_call","tool":"calculator","arguments":{"expression":"25*18"}}
```

Final:
```json
{"type":"final","message":"450."}
```
