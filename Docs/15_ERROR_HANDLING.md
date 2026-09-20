# Error Handling

Categories:
- invalid input
- model timeout
- malformed output
- unknown tool
- invalid arguments
- permission denied
- tool timeout
- tool failure
- network failure

Never hide the actual failure.

Example:
"Couldn't read that file because it is outside the allowed project directory."

A joke may follow only after the factual explanation.

Retry only transient failures. Never blindly retry destructive or external actions.
