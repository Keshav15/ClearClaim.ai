import asyncio
import logging
from config.settings import Settings
from agents.eligibility.eligibility_agent import EligibilityAgent
from agents.evidence.evidence_agent import EvidenceAgent
from agents.filing.filing_agent import FilingAgent
from agents.monitor.monitor_agent import MonitorAgent
from agents.denial_analyzer.denial_analyzer_agent import DenialAnalyzerAgent
from agents.appeal.appeal_agent import AppealAgent

class Orchestrator:
    def __init__(self):
        self.settings = Settings()
        logging.basicConfig(level=self.settings.log_level)
        fhir = self.settings.llm_endpoint.replace('/generate','')  # reuse base URL
        payer = self.settings.llm_endpoint.replace('/generate','')  # you can separate
        self.agents = {
            'eligibility': EligibilityAgent(fhir),
            'evidence': EvidenceAgent(fhir),
            'filing': FilingAgent(payer),
            'monitor': MonitorAgent(payer),
            'analyzer': DenialAnalyzerAgent(),
            'appeal': AppealAgent(payer)
        }

    async def run_pipeline(self, date: str, patient_id: str):
        df = await asyncio.to_thread(self.agents['eligibility'].run, date)
        rec = df.loc[df['needs_auth']].to_dict('records')
        for record in rec:
            evidence = await asyncio.to_thread(self.agents['evidence'].run, record['patient_id'])
            auth_resp = await asyncio.to_thread(self.agents['filing'].run, record, evidence)
            status = await asyncio.to_thread(self.agents['monitor'].run, auth_resp['case_id'])
            if status['state'] == 'Denied':
                denial_info = await asyncio.to_thread(self.agents['analyzer'].run, status['reason'])
                appeal_resp = await asyncio.to_thread(
                    self.agents['appeal'].run, denial_info, evidence
                )

    def start(self, date: str, patient_id: str):
        asyncio.run(self.run_pipeline(date, patient_id))