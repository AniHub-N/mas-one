class SharedMemory:

    def __init__(self):
        self.events = []

    def add_event(
        self,
        timestamp,
        agent,
        event_type,
        target,
        status,
        content,
        confidence,
        supersedes=None
    ):

        self.events.append({
            "timestamp": timestamp,
            "agent": agent,
            "event_type": event_type,
            "target": target,
            "status": status,
            "content": content,
            "confidence": confidence,
            "supersedes": supersedes
        })

    def get_all(self):
        return self.events

    def get_filtered(self, hidden_agents=None):

        if hidden_agents is None:
            hidden_agents = []

        return [
            e for e in self.events
            if e["agent"] not in hidden_agents
        ]

    def pretty_print(self):

        print("\n========== EVENT MEMORY ==========\n")

        for e in self.events:

            print(f"TIME: {e['timestamp']}")
            print(f"AGENT: {e['agent']}")
            print(f"EVENT TYPE: {e['event_type']}")
            print(f"TARGET: {e['target']}")
            print(f"STATUS: {e['status']}")
            print(f"CONFIDENCE: {e['confidence']}")
            print(f"SUPERSEDES: {e['supersedes']}")
            print(f"CONTENT:\n{e['content']}")
            print("\n-----------------------------------\n")

