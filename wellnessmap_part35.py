# === Stage 35: Add active user switching and user-specific records ===
# Project: WellnessMap
import json, os, uuid

class UserStore:
    def __init__(self):
        self.data = {}

    def load(self):
        path = "wellnessmap_users.json"
        if os.path.exists(path):
            with open(path) as f:
                self.data = json.load(f)
        else:
            raise FileNotFoundError("User store not initialized. Run setup first.")

    def save(self):
        with open("wellnessmap_users.json", "w") as f:
            json.dump(self.data, f)

    def add_user(self, name, email):
        uid = str(uuid.uuid4())[:8]
        self.data[uid] = {"name": name, "email": email}
        self.save()
        return uid

    def get_user_records(self, uid):
        user = self.data.get(uid)
        if not user:
            raise KeyError(f"User {uid} does not exist.")
        records_path = f"wellnessmap_{uid}_records.json"
        try:
            with open(records_path) as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_records(self, uid, records):
        with open(f"wellnessmap_{uid}_records.json", "w") as f:
            json.dump(records, f)
