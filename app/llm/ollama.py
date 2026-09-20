import json
import requests
from typing import Iterator, Dict, Any, Optional

from app.config import config

class OllamaClient:
    def __init__(self, base_url: str = None, model: str = None):
        self.base_url = (base_url or config.OLLAMA_BASE_URL).rstrip('/')
        self.model = model or config.MODEL_NAME

    def check_connection(self) -> bool:
        """Check if Ollama is running and accessible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=3)
            return response.status_code == 200
        except requests.RequestException:
            return False
            
    def has_model(self) -> bool:
        """Check if the configured model is available."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=3)
            if response.status_code == 200:
                models = [m.get("name") for m in response.json().get("models", [])]
                return self.model in models
            return False
        except requests.RequestException:
            return False

    def generate(self, prompt: str, system: Optional[str] = None, stream: bool = True) -> Iterator[str]:
        """Generate a response from the model."""
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }
        if system:
            payload["system"] = system

        try:
            with requests.post(url, json=payload, stream=stream, timeout=60) as response:
                response.raise_for_status()
                if stream:
                    for line in response.iter_lines():
                        if line:
                            data = json.loads(line.decode('utf-8'))
                            if "response" in data:
                                yield data["response"]
                else:
                    data = response.json()
                    yield data.get("response", "")
        except requests.RequestException as e:
            yield f"Error communicating with LLM: {str(e)}"
