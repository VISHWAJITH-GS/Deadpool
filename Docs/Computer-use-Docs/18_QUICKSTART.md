# Quickstart

## Prerequisites

Install:
- Python 3.12+
- Ollama
- Qwen3 1.7B

Verify:

```powershell
ollama list
ollama run qwen3:1.7b
```

## Project setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Start

```powershell
python -m app.main
```

## First commands

```text
Open Microsoft Edge.
Open Edge and go to https://leetcode.com
Open VS Code.
What window is currently active?
Stop.
```

## First milestone

Do not add voice or vision-model integration yet.

Make this one workflow extremely reliable:

```text
"Open Edge and go to LeetCode."
```

Then expand to:
- VS Code
- Chrome
- YouTube
- file/project opening
- multi-step workflows
