import time
from utils.helpers import http_get

class MonitorAgent:
    def __init__(self, payer_api: str, poll_interval: int = 3600):
        self.payer_api = payer_api
        self.poll_interval = poll_interval

    def run(self, case_id: str) -> dict:
        while True:
            status = http_get(f"{self.payer_api}/status", params={"case_id": case_id})
            if status["state"] in ["Approved", "Denied"]:
                return status
            time.sleep(self.poll_interval)