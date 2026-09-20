# Definition of Done

The first useful version is complete when:

- [ ] Qwen3 1.7B works through Ollama.
- [ ] CLI accepts natural-language goals.
- [ ] Edge can be launched.
- [ ] Edge can be focused.
- [ ] URLs can be opened directly.
- [ ] Keyboard actions work.
- [ ] Basic mouse actions work.
- [ ] Active window can be detected.
- [ ] Accessibility/UI information can be read where available.
- [ ] Screenshot fallback works.
- [ ] Actions are structured and validated.
- [ ] Every action is permission-checked.
- [ ] Agent verifies task completion.
- [ ] Failed actions do not cause blind loops.
- [ ] Emergency stop works.
- [ ] Destructive actions require confirmation.
- [ ] Memory stores only approved useful information.
- [ ] Personality never claims unverified success.
- [ ] Simple tasks use deterministic fast paths.
- [ ] Latency and action counts are measured.
- [ ] No unrestricted shell/code execution exists.
- [ ] Core tests pass.

## Acceptance example

Input:
"Open Edge and go to LeetCode."

Success:
- Edge becomes active.
- LeetCode is reached.
- task is verified.
- agent stops.
- concise response is returned.
