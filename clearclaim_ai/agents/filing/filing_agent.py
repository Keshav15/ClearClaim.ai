from utils.helpers import http_post
import json

class FilingAgent:
    def __init__(self, payer_api: str):
        self.payer_api = payer_api

    def build_payload(self, record: dict, evidence: str) -> dict:
        return {
            "patient": record,
            "evidence_summary": evidence
        }

    def run(self, record: dict, evidence: str) -> dict:
        payload = self.build_payload(record, evidence)
        # send as JSON to payer endpoint
        return http_post(f"{self.payer_api}/submit_auth", payload)