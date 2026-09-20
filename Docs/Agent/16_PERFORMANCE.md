# Performance Specification

Optimize for successful completion latency.

Fast path:
```text
explicit app type → registry → launch → verify
explicit website type → registry → direct URL → verify
```

Optimization rules:
- cache app discovery
- cache registries
- direct URL navigation
- UI APIs before screenshots
- semantic UI before coordinates
- small prompts
- minimum model calls
- stop after verification
- no unnecessary background polling

Measure:
- total latency
- planner latency
- execution latency
- observation latency
- verification latency
- model calls
- actions
- screenshots
- recovery count
- success rate
