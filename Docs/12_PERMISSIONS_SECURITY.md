# Permissions and Security

## Levels
SAFE — no confirmation.
READ — approved local/web reads.
WRITE — changes local data.
EXTERNAL — external side effects.
DESTRUCTIVE — deletion/irreversible changes.

## MVP policy
SAFE: automatic.
READ: automatic only inside configured scopes.
WRITE/EXTERNAL/DESTRUCTIVE: confirmation.

## Security
- never expose secrets to the model
- validate every tool argument
- restrict file roots
- sanitize tool outputs
- enforce timeouts
- log tool name/status, not sensitive contents
- no arbitrary code execution
