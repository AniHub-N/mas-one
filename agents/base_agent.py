import ollama


class BaseAgent:

    def __init__(self, name, system_prompt):

        self.name = name
        self.system_prompt = system_prompt

    def run(
        self,
        task,
        memory,
        hidden_agents=None
    ):

        # Default empty list
        if hidden_agents is None:
            hidden_agents = []

        # Filter visible events
        events = memory.get_filtered(hidden_agents)

        # Build context
        context = "\n".join([
            f"""
TIMESTAMP: {e['timestamp']}
SOURCE: {e['agent']}
EVENT TYPE: {e['event_type']}
TARGET: {e['target']}
STATUS: {e['status']}
CONFIDENCE: {e['confidence']}
SUPERSEDES: {e['supersedes']}

DETAILS:
{e['content']}
"""
            for e in events
        ])

        prompt = f"""
You are participating in a multi-agent system.

Your role:
{self.system_prompt}

Current Event Memory:
{context}

User Task:
{task}

Reason carefully about:
- temporal ordering
- remediation events
- supersession relationships
- conflicting telemetry
- adversarial misinformation
- current active system state

Do NOT assume all historical events remain active.
"""

        response = ollama.chat(
            model="qwen2.5:1.5b",
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]