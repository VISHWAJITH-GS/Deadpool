# Logging and Observability

Log:
- request ID
- event type
- tool name
- status
- duration
- error category

Never log:
- API keys
- passwords
- full private conversations by default
- file contents
- sensitive memory values

Debug mode may show tool selection, validation result and latency.

Never expose hidden chain-of-thought. Log concise execution metadata only.
