# Product Requirements

## Objective
Build a lightweight local personal agent that feels witty and personal while remaining technically precise.

## Functional requirements
### Conversation
- Text input
- Recent context
- Concise responses
- Streaming when possible

### Agent
- Detect tool need
- Generate structured tool calls
- Validate arguments
- Execute tools
- Feed results back to the model
- Produce final response

### Memory
- Store only explicit user-approved long-term memories
- Retrieve relevant memories
- Delete memories

### Personality
- Default humor level 2/4
- Casual, sarcastic, serious and focus modes
- Personality never changes safety policy
- Never claim failed actions succeeded

### Initial tools
calculator, time/date, system_info, file_search, file_read, web_search adapter.

### Safety
- No arbitrary shell tool in MVP
- Tool allowlist
- Argument schemas
- Permission levels
- Confirmation for modifications/destructive actions

## Performance targets
Engineering targets:
- startup under ~2 seconds excluding model load
- simple local tools under ~200 ms where practical
- stream first token as early as possible
- compact prompts
- avoid unnecessary model calls

## Accuracy
Prefer deterministic tools for calculations/system facts, structured calls, verification and concise prompts.
