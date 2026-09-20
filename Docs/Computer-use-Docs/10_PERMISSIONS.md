# Permissions and Safety

## Levels

### SAFE
Automatic:
- open known apps
- focus windows
- open URLs
- read screen/UI
- keyboard navigation

### CONFIRM
Ask before:
- sending messages
- submitting forms
- posting online
- modifying files
- changing important settings

### DANGEROUS
Always require explicit confirmation:
- delete files
- uninstall applications
- execute arbitrary commands
- change security settings
- perform irreversible operations

## Emergency stop

Provide a global stop mechanism, for example:

```text
Ctrl + Shift + Esc
```

or another configurable hotkey.

Emergency stop must immediately prevent further agent actions.

## Restricted operations

Do not expose:
- arbitrary shell
- arbitrary Python
- unrestricted filesystem write
- credential extraction
- password handling
- security bypasses
