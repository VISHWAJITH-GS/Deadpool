# Observation and UI Understanding

Observation hierarchy:

1. Window state
   - active window
   - title
   - application identity
   - bounds

2. Accessibility/UI tree
   - buttons
   - text fields
   - links
   - menus
   - checkboxes
   - labels
   - state

3. Screenshot
   - use only when UI semantics are insufficient

4. Vision
   - only when deterministic observation cannot solve the task

Prefer semantic UI targets over coordinates.

Example:

```json
{
  "role":"button",
  "name":"Submit",
  "enabled":true,
  "visible":true
}
```

Do not continuously record the desktop. Capture only when needed.
