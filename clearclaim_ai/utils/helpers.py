import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from config.settings import Settings

settings = Settings()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def http_get(path: str, params: dict = None) -> dict:
    headers = {"Authorization": f"Bearer {settings.llm_api_key}"}
    resp = requests.get(path, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def http_post(path: str, json: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type": "application/json"
    }
    resp = requests.post(path, headers=headers, json=json)
    resp.raise_for_status()
    return resp.json()