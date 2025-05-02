from typing import List, Dict
from utils.helpers import http_get
from models.llm_models import LLMModel

class EvidenceAgent:
    def __init__(self, fhir_url: str):
        self.fhir_url = fhir_url
        self.llm = LLMModel()

    def fetch_reports(self, patient_id: str) -> List[Dict]:
        return http_get(f"{self.fhir_url}/Observation", params={"patient": patient_id})

    def summarize(self, reports: List[Dict]) -> str:
        text = "\n".join(r["text"] for r in reports)
        prompt = f"Summarize key medical necessity arguments from:\n{text}"
        return self.llm.complete(prompt)

    def run(self, patient_id: str) -> str:
        reports = self.fetch_reports(patient_id)
        return self.summarize(reports)