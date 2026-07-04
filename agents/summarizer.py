from agents.base_agent import BaseAgent


class SummarizerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Summarizer",
            """
You are a summarization agent.

Your responsibilities:
- compress important information
- provide concise findings
- preserve critical details
- preserve uncertainty when present
"""
        )