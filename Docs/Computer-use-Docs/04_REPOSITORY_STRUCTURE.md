# Repository Structure

```text
deadpool-agent/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── runtime/
│   │   ├── agent.py
│   │   ├── state.py
│   │   └── limits.py
│   ├── llm/
│   │   └── ollama_client.py
│   ├── planner/
│   │   ├── planner.py
│   │   └── schemas.py
│   ├── observer/
│   │   ├── windows.py
│   │   ├── ui_tree.py
│   │   └── screenshot.py
│   ├── executor/
│   │   ├── keyboard.py
│   │   ├── mouse.py
│   │   ├── apps.py
│   │   └── browser.py
│   ├── verifier/
│   │   └── verifier.py
│   ├── permissions/
│   │   └── policy.py
│   ├── memory/
│   │   ├── store.py
│   │   └── retrieval.py
│   ├── persona/
│   │   └── persona.py
│   └── tools/
│       └── registry.py
├── tests/
├── data/
│   └── agent.db
├── logs/
├── .env.example
├── requirements.txt
└── README.md
```

Keep each module small and independently testable.
