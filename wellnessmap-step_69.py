# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: WellnessMap
import random, json


def reset_demo_data(db):
    """Reset demo data for manual testing: clear all tables and re-insert a fixed small dataset."""
    db["routines"] = [
        {"id": 1, "name": "Morning stretch", "schedule": "07:00"},
        {"id": 2, "name": "Evening walk", "schedule": "19:00"},
    ]
    db["symptoms"] = [
        {"id": 1, "name": "Headache", "severity": 3},
        {"id": 2, "name": "Fatigue", "severity": 4},
    ]
    db["measurements"] = [
        {"id": 1, "routine_id": 1, "symptom_id": 1, "value": random.randint(50, 90), "timestamp": "2026-03-17T07:30"},
        {"id": 2, "routine_id": 1, "symptom_id": 2, "value": random.randint(40, 80), "timestamp": "2026-03-17T07:35"},
    ]
    db["reminders"] = [
        {"id": 1, "routine_id": 1, "enabled": True},
        {"id": 2, "routine_id": 2, "enabled": False},
    ]
    db["trends"] = []
    return db


if __name__ == "__main__":
    from wellness_map import WellnessMap
    app = WellnessMap()
    demo_db = {k: [] for k in ["routines", "symptoms", "measurements", "reminders", "trends"]}
    reset_demo_data(demo_db)
    print("Demo data reset OK:", json.dumps(demo_db, indent=2))
