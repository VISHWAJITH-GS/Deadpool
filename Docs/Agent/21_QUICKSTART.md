# Quickstart

Prerequisites:
- Windows 10/11
- Python 3.12+
- Ollama
- Qwen3 1.7B

```powershell
ollama list
ollama run qwen3:1.7b
```

Create environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run:

```powershell
python -m app.main
```

First tests:

```text
Open Chrome app.
Open Microsoft Word app.
Open LeetCode website.
Open Chrome app and go to LeetCode website.
Open Chrome app, go to LeetCode website, find Two Sum.
```

Do not add voice, vision-model integration or proactive behavior until these workflows are reliable.
