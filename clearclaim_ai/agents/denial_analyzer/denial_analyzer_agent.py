from models.llm_models import LLMModel

class DenialAnalyzerAgent:
    def __init__(self):
        self.llm = LLMModel()

    def run(self, denial_text: str) -> dict:
        prompt = (
            f"Extract structured missing elements from this denial reason:\n{denial_text}"  
        )
        response = self.llm.complete(prompt)
        # assume JSON string returned
        return eval(response)