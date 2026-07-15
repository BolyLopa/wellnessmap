# === Stage 19: Add undo support for the last simple mutation ===
# Project: WellnessMap
class SimpleUndo:
    def __init__(self):
        self.history = []

    def record(self, state_before, action_name=""):
        self.history.append({"state": state_before, "action": action_name})

    def undo(self):
        if not self.history:
            return None
        entry = self.history.pop()
        return entry["state"]

    def clear(self):
        self.history.clear()
