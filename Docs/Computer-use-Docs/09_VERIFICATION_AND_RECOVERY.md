# Verification and Recovery

An action is not successful merely because it executed without an exception.

## Example

Goal:
"Open Edge and go to LeetCode."

Bad verification:
"Enter key was pressed."

Good verification:
- Edge is active
- page title/domain indicates LeetCode
- or browser state confirms target URL

## Recovery

If navigation fails:

```text
observe
 ↓
determine cause
 ↓
retry with a different safe method
```

Example:

```text
open_url failed
 ↓
focus Edge
 ↓
Ctrl+L
 ↓
type URL
 ↓
Enter
 ↓
verify
```

If verification still fails:
- stop
- explain what happened
- do not keep clicking randomly

## Anti-loop rule

Never repeat the same failed action more than once without new information.
