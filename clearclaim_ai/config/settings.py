from pydantic import BaseSettings

class Settings(BaseSettings):
    # URL of your GCP-hosted LLM endpoint
    llm_endpoint: str
    # API key or token if your VM requires auth
    llm_api_key: str
    log_level: str = "INFO"
    max_retries: int = 3

    class Config:
        env_file = ".env"