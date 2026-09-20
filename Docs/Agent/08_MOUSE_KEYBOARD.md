# Mouse and Keyboard Control

Keyboard:
- key press
- hotkey
- text entry

Mouse:
- move
- click
- double click
- right click
- scroll
- drag when safe

Execution pipeline:
1. schema validation
2. permission check
3. bounds/timeout check
4. execute
5. verify when required

Prefer semantic UI elements over coordinates. Treat coordinates as a fallback and never blindly reuse stale coordinates.
