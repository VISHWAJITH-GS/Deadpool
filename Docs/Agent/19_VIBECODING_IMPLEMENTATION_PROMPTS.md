# Vibecoding Implementation Prompts

Build milestone by milestone.

## 1 — Skeleton
Create the Python Windows repository, CLI, configuration, logging, state machine and tests. Do not add arbitrary command execution.

## 2 — Registry
Implement application/website registries, aliases, installed-app discovery and caching.

## 3 — Fast Path
Implement explicit app/website target parsing and deterministic execution without an LLM where possible.

## 4 — Desktop Control
Implement app launch/focus, keyboard and mouse control with validation and limits.

## 5 — Observation
Implement active-window and UI/accessibility observation. Add screenshot fallback.

## 6 — Browser
Implement direct URL navigation and browser-state verification.

## 7 — Qwen
Connect Ollama/Qwen3 1.7B. Require structured JSON plans and reject unknown tools.

## 8 — Agent Loop
Implement observe → plan → permission → execute → observe → verify → recover.

## 9 — Safety
Implement risk levels, confirmations, emergency stop and execution limits.

## 10 — Multi-Step
Support "Open Chrome, go to LeetCode, find Two Sum."

## 11 — Memory
Add SQLite for explicit aliases, locations and workflows.

## 12 — Persona
Add the Deadpool-style response layer after verification.

## 13 — Performance
Measure and reduce model calls, screenshots and unnecessary actions.

Coding-agent rules:
- inspect existing files first
- make small changes
- avoid large frameworks
- never expose arbitrary shell/Python execution
- run tests after each milestone
- preserve working behavior
- explain new dependencies
