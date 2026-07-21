# === Stage 40: Add plain text report export ===
# Project: WellnessMap
def export_report(self, filepath='wellness_report.txt'):
    with open(filepath, 'w') as f:
        f.write('=== Wellness Report ===\n\n')
        for r in self.routines:
            f.write(f"Routine: {r.name}\n")
            if hasattr(r, 'next_time'):
                f.write(f"Next run: {r.next_time}\n")
        for s in self.symptoms:
            f.write(f"\nSymptom: {s.name}, severity: {s.severity}\n")
        for m in self.measurements:
            f.write(f"\nMeasurement: {m.label} = {m.value}\n")
        for rem in self.reminders:
            f.write(f"\nReminder: {rem.text} at {rem.time}\n")
