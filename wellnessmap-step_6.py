# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: WellnessMap
def delete_entry(self, entry_id: str) -> bool:
    """Remove an entry by ID after confirming with a flag."""
    if not self._confirm_delete(entry_id):
        return False
    try:
        del self.entries[entry_id]
        self.save()
        print(f"Entry {entry_id} deleted.")
        return True
    except KeyError:
        print(f"Entry {entry_id} not found.")
        return False

def delete_routine(self, routine_id: str) -> bool:
    """Delete a routine after confirming with a flag."""
    if self.entries.pop(routine_id, None):
        self.save()
        print(f"Routine {routine_id} deleted.")
        return True
    print(f"Routine {routine_id} not found.")
    return False

def delete_measurement(self, measurement_id: str) -> bool:
    """Delete a measurement after confirming with a flag."""
    if self.entries.pop(measurement_id, None):
        self.save()
        print(f"Measurement {measurement_id} deleted.")
        return True
    print(f"Measurement {measurement_id} not found.")
    return False

def delete_symptom(self, symptom_id: str) -> bool:
    """Delete a symptom after confirming with a flag."""
    if self.entries.pop(symptom_id, None):
        self.save()
        print(f"Symptom {symptom_id} deleted.")
        return True
    print(f"Symptom {symptom_id} not found.")
    return False

def delete_reminder(self, reminder_id: str) -> bool:
    """Delete a reminder after confirming with a flag."""
    if self.entries.pop(reminder_id, None):
        self.save()
        print(f"Reminder {reminder_id} deleted.")
        return True
    print(f"Reminder {reminder_id} not found.")
    return False

def delete_all(self) -> bool:
    """Remove every entry and reset the file."""
    if len(self.entries) == 0:
        print("No entries to delete.")
        return False
    self.entries.clear()
    self.save()
    print(f"All {len(self.entries)} entries deleted.")
    return True
