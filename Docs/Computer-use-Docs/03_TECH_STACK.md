# Lightweight Technical Stack

## Required

- Windows 10/11
- Python 3.12+
- Ollama
- Qwen3 1.7B
- SQLite
- standard-library Python wherever practical

## Desktop automation

Recommended hierarchy:

1. Windows UI Automation / accessibility APIs
2. deterministic keyboard/mouse automation
3. screenshot/OCR fallback
4. vision model only when genuinely necessary

Do not make screenshot analysis the default path.

## UI

CLI first.

A GUI can be added later without changing the agent runtime.

## Network

Normal operation should work locally.

Internet access is only required for web-related tasks.

## Dependency policy

Every new dependency must justify:
- capability gained
- latency cost
- memory cost
- maintenance cost

Avoid large agent frameworks for the core runtime.
