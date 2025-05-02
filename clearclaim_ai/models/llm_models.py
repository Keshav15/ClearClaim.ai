from utils.helpers import http_post
from config.settings import Settings

settings = Settings()

class LLMModel:
    """Wrapper for your self-hosted LLM."""
    def __init__(self):
        self.endpoint = settings.llm_endpoint

    def complete(self, prompt: str, max_tokens: int = 512, temperature: float = 0.0) -> str:
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        response = http_post(f"{self.endpoint}/generate", payload)
        return response.get("text", "")