# Action Schema

All computer actions must use structured data.

Example:

```json
{
  "action": "launch_app",
  "arguments": {
    "name": "Microsoft Edge"
  }
}
```

Other examples:

```json
{"action":"focus_window","arguments":{"title_contains":"Edge"}}
```

```json
{"action":"hotkey","arguments":{"keys":["CTRL","L"]}}
```

```json
{"action":"type_text","arguments":{"text":"https://leetcode.com"}}
```

```json
{"action":"press_key","arguments":{"key":"ENTER"}}
```

```json
{"action":"click","arguments":{"x":500,"y":300}}
```

```json
{"action":"open_url","arguments":{"url":"https://leetcode.com"}}
```

## Action categories

SAFE:
- launch known app
- focus known window
- open approved URL
- keyboard navigation
- screenshot

CONTROL:
- mouse click
- typing
- scrolling

WRITE:
- editing files
- submitting forms
- sending content

DESTRUCTIVE:
- delete
- uninstall
- system configuration changes

## Validation

Every action must be:
1. parsed
2. schema validated
3. permission checked
4. bounded
5. executed
6. optionally verified
