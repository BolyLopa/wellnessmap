# === Stage 60: Add saved views for frequently used filters ===
# Project: WellnessMap
class SavedView:
    """Compact saved view for frequently used filter combinations."""

    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}  # e.g. {"symptom": "headache", "timeframe": "week"}

    def apply(self, routine_data, symptom_data, measurement_data, reminder_data):
        """Apply saved filter set to all data and return filtered records."""
        if not self.filters:
            return (routine_data, symptom_data, measurement_data, reminder_data)

        routines = [r for r in routine_data if r.get("symptom") == self.filters.get("symptom")]
        symptoms = [s for s in symptom_data if s.get("name") == self.filters.get("symptom")]
        measurements = [m for m in measurement_data]
        reminders = [rem for rem in reminder_data if self.filters.get("timeframe", "") not in rem.get("notes", "")]
        return (routines, symptoms, measurements, reminders)

    def __str__(self):
        return f"SavedView(name={self.name!r}, filters={self.filters})"


# Example usage: register saved views for common wellness check patterns
saved_views = {
    "Morning Check": SavedView("Morning Check", {"timeframe": "morning"}),
    "Afternoon Review": SavedView("Afternoon Review", {"symptom": None, "timeframe": "afternoon"}),
    "Weekly Symptoms": SavedView("Weekly Symptoms", {"timeframe": "week"}),
}


def get_saved_view(name):
    """Retrieve a saved view by name."""
    return saved_views.get(name)


if __name__ == "__main__":
    print(saved_views["Morning Check"])  # SavedView(name='Morning Check', filters={'timeframe': 'morning'})
