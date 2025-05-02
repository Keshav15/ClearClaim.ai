from models.llm_models import LLMModel
from utils.helpers import http_post

class AppealAgent:
    def __init__(self, payer_api: str):
        self.payer_api = payer_api
        self.llm = LLMModel()

    def draft_appeal(self, denial_info: dict, extra_data: str) -> str:
        prompt = (
            "Draft an appeal letter given denial info and extra evidence:\n"
            f"{denial_info}\nExtra data:\n{extra_data}"
        )
        return self.llm.complete(prompt)

    def run(self, denial_info: dict, extra_data: str) -> dict:
        letter = self.draft_appeal(denial_info, extra_data)
        payload = {"case": denial_info, "appeal_text": letter}
        return http_post(f"{self.payer_api}/submit_appeal", payload)