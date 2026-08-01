# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: WellnessMap
from datetime import date, timedelta

class WellnessMapValidationReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def check_date_range(self):
        today = date.today()
        if today > date(2025, 3, 1):
            self.warnings.append("Date range exceeds reference period")

    def check_morning_reminder(self):
        if not any(r.reminder == "morning" for r in Routine.reminders):
            self.errors.append("Missing morning reminder routine")

    def check_symptom_tracking(self):
        if not any(s.name == "symptoms" for s in SymptomTracker.symptoms):
            self.warnings.append("Symptom tracker not initialized")

    def check_measurement_types(self):
        expected = {"heart_rate", "steps", "weight"}
        actual = set(Measurement.measurements.keys())
        missing = expected - actual
        if missing:
            self.errors.append(f"Missing measurement types: {missing}")

    def generate_report(self):
        self.check_date_range()
        self.check_morning_reminder()
        self.check_symptom_tracking()
        self.check_measurement_types()
        report = f"""WellnessMap Validation Report ({date.today()})
Warnings: {len(self.warnings)}
- {"; ".join(self.warnings) if self.warnings else "None"}
Errors: {len(self.errors)}
- {"; ".join(self.errors) if self.errors else "None"}
Status: {'PASS' if not self.errors else 'FAIL'}"""
        return report

report = WellnessMapValidationReport()
print(report.generate_report())
