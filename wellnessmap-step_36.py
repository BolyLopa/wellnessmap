# === Stage 36: Add templates for quickly creating common records ===
# Project: WellnessMap
class RecordTemplates:
    """Pre-built templates for common wellness records."""

    @staticmethod
    def daily_log_entry(date=None):
        return {
            "date": date or datetime.now().date(),
            "mood": None,
            "energy_level": None,
            "notes": "",
        }

    @staticmethod
    def symptom_record(symptom_name, severity=1, duration_minutes=None, notes=""):
        return {
            "symptom": symptom_name,
            "severity": severity,
            "duration_minutes": duration_minutes,
            "notes": notes,
            "timestamp": datetime.now(),
        }

    @staticmethod
    def measurement_recording(measurement_type, value, unit="unit", notes=""):
        return {
            "type": measurement_type,
            "value": value,
            "unit": unit,
            "notes": notes,
            "timestamp": datetime.now(),
        }

    @staticmethod
    def routine_checkpoint(routine_name, completed=True, duration_minutes=None):
        return {
            "routine": routine_name,
            "completed": completed,
            "duration_minutes": duration_minutes,
            "timestamp": datetime.now(),
        }

    @staticmethod
    def reminder_entry(reminder_type, message, scheduled_time=None):
        return {
            "type": reminder_type,
            "message": message,
            "scheduled_time": scheduled_time or datetime.now(),
        }

    @staticmethod
    def trend_summary_period(start_date, end_date, measurement_types, category="daily"):
        return {
            "start_date": start_date,
            "end_date": end_date,
            "measurement_types": measurement_types,
            "category": category,
        }
