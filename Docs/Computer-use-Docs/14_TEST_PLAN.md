# Test Plan

## Unit tests

Test:
- action schema validation
- permission policy
- application registry
- URL validation
- keyboard mappings
- path restrictions
- state transitions
- retry limits

## Integration tests

### Test 1
"Open Edge."

Expected:
Edge launches or becomes focused.

### Test 2
"Open Edge and go to LeetCode."

Expected:
Edge active and LeetCode reached.

### Test 3
"Open VS Code."

Expected:
VS Code active.

### Test 4
"Open Edge, go to LeetCode, then stop."

Expected:
agent stops before additional actions.

### Test 5
Invalid application name.

Expected:
clear failure; no random application launch.

### Test 6
Navigation failure.

Expected:
one recovery attempt, then controlled failure.

### Test 7
Destructive action.

Expected:
confirmation required.

## Performance test

Run each task at least 20 times and record:
- median latency
- p95 latency
- model calls
- action count
- failure rate

Do not optimize only for raw speed; successful completion matters.
