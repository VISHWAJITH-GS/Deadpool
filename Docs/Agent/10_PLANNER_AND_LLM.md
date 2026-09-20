# Planner and Qwen3 1.7B

Use Qwen for:
- goal interpretation
- ambiguous target resolution
- multi-step planning
- next-action decisions when deterministic rules are insufficient
- safe recovery reasoning

Do not use Qwen for:
- launching a known app
- opening a known URL
- pressing a known key
- reading a registry entry

Require structured JSON:

```json
{
  "goal":"Open Chrome and go to LeetCode",
  "steps":[
    {"action":"open","target":"Chrome","type":"app"},
    {"action":"navigate","target":"LeetCode","type":"website"}
  ]
}
```

Validate every model response before execution. Keep prompts small: goal, current state, available actions, relevant registry entries and current step.
