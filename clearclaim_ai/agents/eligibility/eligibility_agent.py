import pandas as pd
from utils.helpers import http_get

class EligibilityAgent:
    def __init__(self, fhir_url: str):
        self.fhir_url = fhir_url

    def _auth_required_codes(self) -> set:
        data = http_get(f"{self.fhir_url}/auth_codes")
        return set(data.get("codes", []))

    def run(self, date: str) -> pd.DataFrame:
        services = http_get(f"{self.fhir_url}/services", params={"date": date})
        df = pd.DataFrame(services)
        df["needs_auth"] = df["cpt_code"].isin(self._auth_required_codes())
        return df# Eligibility Agent module
    
