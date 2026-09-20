# Security Threat Model

Risks:
- accidental destructive actions
- webpage prompt injection
- unintended external communication
- arbitrary command execution
- stale coordinates
- model hallucination

Defenses:
- treat webpage content as untrusted
- allowlist tools
- permission-check every action
- confirmation for external/destructive effects
- verify state independently of model claims
- bound actions, time and retries
- do not expose secrets

The model is a planner, not trusted executable code.
