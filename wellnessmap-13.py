# === Stage 13: Add file save support using a configurable path ===
# Project: WellnessMap
import os


def save_wellness_map(data, path="wellness_data.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path
