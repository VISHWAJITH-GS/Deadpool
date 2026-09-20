# Configuration

Example `.env`:

```env
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=qwen3:1.7b
DB_PATH=./data/agent.db
LOG_LEVEL=INFO
HUMOR_LEVEL=0.7
DEFAULT_MODE=CASUAL
```

Use environment variables for machine-specific settings. Do not hard-code secrets or machine-specific paths.
