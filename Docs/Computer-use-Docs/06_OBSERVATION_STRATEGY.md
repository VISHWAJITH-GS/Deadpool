# Observation Strategy

The agent needs to know what is currently happening on the desktop.

## Priority order

### 1. Application/window state

Use OS APIs to determine:
- running processes where permitted
- active window
- window title
- application identity

This is cheap and fast.

### 2. Accessibility/UI tree

Read available UI elements:
- buttons
- text fields
- links
- menus
- window names

Prefer semantic element targeting over coordinates.

### 3. Deterministic state

Use known facts:
- URL from browser integration when available
- process state
- window title
- known application state

### 4. Screenshot

Capture only when necessary.

Use screenshots for:
- unknown visual UI
- custom-drawn controls
- verification when semantic UI data is insufficient

## Important

Do not continuously capture screenshots.

Default:
- observe only when needed
- capture the smallest useful region if possible
- discard images after task completion unless the user explicitly asks to save them
