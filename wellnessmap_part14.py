# === Stage 14: Add file load support with fallback demo data ===
# Project: WellnessMap
def load_wellness_data(filepath=None):
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        demo_data = {
            "user": {"name": "Alice", "age": 28},
            "measurements": [
                {"date": "2024-01-05", "type": "sleep_hours", "value": 7.2, "unit": "hours"},
                {"date": "2024-01-10", "type": "sleep_hours", "value": 6.8, "unit": "hours"},
                {"date": "2024-01-15", "type": "sleep_hours", "value": 7.5, "unit": "hours"}
            ],
            "routines": [
                {"name": "Morning Stretch", "time": "07:00"},
                {"name": "Evening Walk", "time": "19:30"}
            ],
            "symptoms": [
                {"date": "2024-01-12", "type": "headache", "severity": 3},
                {"date": "2024-01-20", "type": "fatigue", "severity": 5}
            ],
            "reminders": [
                {"text": "Drink water every hour", "time": "09:00"},
                {"text": "Take vitamins", "time": "08:30"}
            ]
        }
    return data
