# Test Plan

Unit tests:
- parser
- target types
- registry lookup
- aliases
- action schemas
- permissions
- state transitions
- retry limits
- URL validation

Integration:
1. Open Chrome app.
2. Open LeetCode website.
3. Open Chrome app and go to LeetCode.
4. Open Chrome, go to LeetCode, find Two Sum.
5. Unknown application.
6. Navigation failure.
7. Delete-file confirmation.
8. Webpage prompt injection.

Expected: controlled execution, verification, safe recovery and no blind loops.

Performance: run representative tasks 20+ times and record median/p95 latency, success rate, model calls, screenshots and action count.
