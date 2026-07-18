# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: WellnessMap
class ReminderHelper:
    def __init__(self, reminders_db):
        self.reminders_db = reminders_db
    
    def get_upcoming_reminders(self, now=None):
        if now is None:
            from datetime import datetime
            now = datetime.now()
        upcoming = []
        for reminder in self.reminders_db:
            due_date = reminder.get('due_date') or reminder.get('scheduled_at')
            if isinstance(due_date, str) and not isinstance(due_date, datetime):
                from dateutil.parser import parse as parse_date
                due_date = parse_date(due_date)
            if due_date > now:
                upcoming.append({
                    'reminder': reminder,
                    'days_until': (due_date - now).total_seconds() / 86400
                })
        return sorted(upcoming, key=lambda x: x['days_until'])
