# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: WellnessMap
import random, datetime

class WellnessMap:
    def __init__(self):
        self.routines = []
        self.symptoms = []
        self.measurements = []
        self.reminders = []
        self.users = {}
        self._seed_demo()
    
    def _seed_demo(self):
        for i in range(1, 4):
            uid = f"user_{i}"
            self.users[uid] = {"name": f"User {i}", "created_at": datetime.datetime.utcnow()}
        
        routines = [
            ("Morning Stretch", "exercise", 700),
            ("Meditation", "wellness", 600),
            ("Hydration", "hydration", 300),
            ("Sleep Log", "sleep", 2300),
        ]
        for name, category, time_h in routines:
            self.routines.append({
                "name": name,
                "category": category,
                "target_time": datetime.time(time_h),
                "active_users": [uid for uid in self.users],
                "completed_today": {uid: False for uid in self.users}
            })
        
        sample_symptoms = ["Headache", "Fatigue", "Insomnia", "Mood Low"]
        sample_measurements = ["Heart Rate", "Steps", "Calories", "Sleep Hours"]
        today = datetime.date.today()
        
        for i in range(7):
            date = today + datetime.timedelta(days=i)
            self.measurements.append({
                "date": date,
                "measurements": {m: random.randint(100, 500) if m != "Sleep Hours" else random.choice([4.5, 6.0, 7.5]) for m in sample_measurements}
            })
        
        for uid in self.users:
            self.reminders.append({
                "user": uid,
                "message": f"{uid}, don't forget your morning stretch!",
                "scheduled_time": datetime.datetime.utcnow(),
                "status": "pending"
            })

    def get_trend_summary(self, measurement_type="Heart Rate", days=7):
        recent = [d for d in self.measurements if (datetime.date.today() - datetime.timedelta(days=days)).date() <= d["date"]]
        values = []
        for r in recent:
            v = r["measurements"].get(measurement_type, None)
            if v is not None:
                values.append(v)
        return {
            "measurement": measurement_type,
            "days": days,
            "count": len(values),
            "avg": sum(values)/len(values) if values else 0,
            "min": min(values) if values else 0,
            "max": max(values) if values else 0
        }

    def add_reminder(self, user_id, message):
        self.reminders.append({
            "user": user_id,
            "message": message,
            "scheduled_time": datetime.datetime.utcnow(),
            "status": "pending"
        })
