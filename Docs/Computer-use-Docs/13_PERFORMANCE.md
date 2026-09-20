# Performance Plan

## Main latency sources

1. LLM inference
2. screenshots/vision
3. unnecessary actions
4. unnecessary model calls
5. network access

## Optimization rules

### Use deterministic shortcuts

"Open Edge" → launch application.

"Go to LeetCode" → direct URL.

"Press Ctrl+S" → keyboard event.

### Keep Qwen prompts small

Send only:
- current goal
- current state
- relevant action schema
- minimal recent context

### Avoid vision unless necessary

A screenshot + vision model should be a fallback, not the normal path.

### Stop early

Once success is verified, stop immediately.

## Metrics

Measure:
- time to first model token
- planning latency
- action latency
- observation latency
- verification latency
- total task latency
- number of model calls
- number of actions
- recovery count

Target behavior:
- simple task: preferably one model decision or deterministic shortcut
- normal task: minimal model/action cycles
- no background polling unless explicitly required
