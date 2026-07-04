from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Planner",
            """
You are a planning agent.

Your job:
- break tasks into steps
- identify important information needed
- guide the workflow logically
"""
        )