# === Stage 18: Add an activity log with timestamps and action names ===
# Project: WellnessMap
class ActivityLog:
    """Compact log of user actions with timestamps and action names."""
    
    def __init__(self):
        self.entries = []
        
    def record(self, action_name, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        entry = {
            "timestamp": timestamp,
            "action": action_name
        }
        self.entries.append(entry)
        return entry
    
    def log_routine_completion(self, routine_name):
        return self.record(f"Routine completed: {routine_name}")
    
    def log_symptom_report(self, symptom_type):
        return self.record(f"Symptom reported: {symptom_type}")
    
    def log_measurement(self, metric_name):
        return self.record(f"Measurement taken: {metric_name}")
        
    def log_reminder_ack(self, reminder_text):
        return self.record(f"Reminder acknowledged: {reminder_text}")
    
    def get_recent_activities(self, limit=10):
        recent = self.entries[-limit:] if len(self.entries) > limit else self.entries[:]
        return sorted(recent, key=lambda x: x["timestamp"], reverse=True)[:limit]
    
    def summary(self):
        counts = {}
        for entry in self.entries:
            action = entry.get("action", "unknown")
            counts[action] = counts.get(action, 0) + 1
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)
