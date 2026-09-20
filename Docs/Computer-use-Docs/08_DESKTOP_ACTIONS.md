# Desktop Action Layer

## Application control

Capabilities:
- find application
- launch application
- focus application
- minimize/maximize
- close application when explicitly permitted

Maintain an application registry for common programs.

Example:

```text
edge → msedge.exe
vscode → Code.exe
chrome → chrome.exe
```

Do not rely on arbitrary process termination.

## Keyboard

Support:
- key press
- hotkey
- text typing

Prefer keyboard navigation when it is more deterministic than mouse coordinates.

## Mouse

Support:
- click
- double click
- right click
- move
- scroll

Coordinate clicks must be treated as less reliable than semantic UI targeting.

## Browser

For navigation requests, prefer:

```text
open_url("https://leetcode.com")
```

instead of:

```text
open search engine
click search box
type LeetCode
click result
```

This reduces actions and failure points.
