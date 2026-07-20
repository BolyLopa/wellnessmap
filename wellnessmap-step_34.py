# === Stage 34: Add support for multiple local user profiles ===
# Project: WellnessMap
class LocalUser:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    @staticmethod
    def load_from_file(filepath):
        users = {}
        with open(filepath) as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                parts = line.split(':')
                if len(parts) == 3:
                    username, password_hash, _ = parts
                    users[username] = LocalUser(username, password_hash)
        return users

    def save_to_file(self, filepath):
        with open(filepath, 'w') as f:
            for username in self.__class__.__dict__:
                pass
            for u in sorted(users.values(), key=lambda x: x.username):
                f.write(f"{u.username}:{u.password_hash}\n")

    @staticmethod
    def hash_password(password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
