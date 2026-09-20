# System Architecture

```text
USER
  |
  v
Command Parser
  |
  v
Target Resolver
  |----------------------|
  |                      |
Fast deterministic      Qwen3 1.7B
path                    planner
  |                      |
  +----------+-----------+
             |
             v
        Agent Runtime
             |
       +-----+------+
       |            |
       v            v
    Observer     Planner
       |            |
       +-----+------+
             |
             v
          Executor
       /     |      \
      /      |       \
   Apps   Browser   Input
                     |
             Keyboard/Mouse
                     |
                     v
                  Windows
                     |
                     v
                  Verify
                     |
             +-------+-------+
             |               |
           Success         Failure
             |               |
            DONE          Recovery
```

Design rule: the LLM determines intent and plans; deterministic software performs computer operations. Never execute arbitrary model-generated code.

Modules:
- parser
- registry
- planner
- observer
- executor
- verifier
- permissions
- runtime
- memory
- persona
