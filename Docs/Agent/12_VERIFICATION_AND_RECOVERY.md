# Verification and Recovery

An executor returning successfully does not prove the task succeeded.

For "Open LeetCode website", verify:
- browser is active
- current page/title/domain matches LeetCode

Recovery:
1. observe current state
2. determine cause
3. perform one safe alternative
4. verify again
5. stop after bounded retries

Never repeat an identical failed action without new information.

Only report success after verification.
