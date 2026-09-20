import os

class Config:
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_NAME = os.getenv("MODEL_NAME", "qwen3:1.7b")
    DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "agent.db")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

config = Config()
