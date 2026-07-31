# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: WellnessMap
import random

SEED = 42
random.seed(SEED)


def seed_demo_data() -> dict:
    """Generate deterministic sample data for WellnessMap."""
    routines = [
        {"id": "r1", "name": "Morning Stretch", "time": "07:00"},
        {"id": "r2", "name": "Hydration Break", "time": "10:30"},
        {"id": "r3", "name": "Evening Reflection", "time": "21:00"},
    ]

    symptoms = [
        {"id": "s1", "name": "Headache", "severity_levels": ["mild", "moderate", "severe"]},
        {"id": "s2", "name": "Fatigue", "severity_levels": ["low", "medium", "high"]},
    ]

    measurements = [
        {"id": "m1", "name": "Heart Rate", "unit": "bpm"},
        {"id": "m2", "name": "Blood Pressure", "unit": "mmHg"},
    ]

    reminders = [
        {"id": "rem1", "routine_id": "r1", "message": "Don't forget to stretch!", "enabled": True},
        {"id": "rem2", "routine_id": "r3", "message": "Time for reflection.", "enabled": False},
    ]

    return {
        "routines": routines,
        "symptoms": symptoms,
        "measurements": measurements,
        "reminders": reminders,
    }


demo = seed_demo_data()
print(f"Seeded {len(demo['routines'])} routines, {len(demo['symptoms'])} symptoms, "
      f"{len(demo['measurements'])} measurements, and {len(demo['reminders'])} reminders.")
