# Repository Structure

```text
deadpool/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── runtime/
│   │   ├── agent.py
│   │   ├── state.py
│   │   └── limits.py
│   ├── parser/
│   │   ├── parser.py
│   │   └── schemas.py
│   ├── llm/
│   │   └── ollama.py
│   ├── registry/
│   │   ├── apps.py
│   │   ├── websites.py
│   │   ├── aliases.py
│   │   └── discovery.py
│   ├── observer/
│   │   ├── desktop.py
│   │   ├── windows_ui.py
│   │   ├── browser.py
│   │   └── screenshot.py
│   ├── planner/
│   │   └── planner.py
│   ├── executor/
│   │   ├── apps.py
│   │   ├── browser.py
│   │   ├── keyboard.py
│   │   └── mouse.py
│   ├── verifier/
│   │   └── verifier.py
│   ├── permissions/
│   │   └── policy.py
│   ├── memory/
│   │   └── store.py
│   └── persona/
│       └── response.py
├── tests/
├── data/
├── logs/
├── requirements.txt
└── README.md
```
