# Repository Structure

```text
deadpool-agent/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── agent/
│   │   ├── runtime.py
│   │   ├── planner.py
│   │   ├── context.py
│   │   └── persona.py
│   ├── llm/
│   │   └── ollama.py
│   ├── tools/
│   │   ├── registry.py
│   │   ├── calculator.py
│   │   ├── datetime_tool.py
│   │   ├── system_info.py
│   │   ├── files.py
│   │   └── web.py
│   ├── memory/
│   │   ├── store.py
│   │   └── retrieval.py
│   └── schemas/
│       └── actions.py
├── tests/
├── data/
│   └── agent.db
├── .env.example
├── requirements.txt
└── README.md
```

Keep modules small and prefer the standard library when practical.
