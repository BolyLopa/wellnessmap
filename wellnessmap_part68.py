# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: WellnessMap
def generate_changelog(activity_log):
    """Generate a compact changelog from activity log entries."""
    lines = []
    for entry in activity_log:
        date = entry.get("date", "Unknown")
        description = entry.get("description", "")
        if description:
            lines.append(f"- {date}: {description}")
    return "\n".join(lines)

activity_log = [
    {"date": "2024-11-01", "description": "Initial project setup and data models"},
    {"date": "2024-11-05", "description": "Added symptom tracking functionality"},
    {"date": "2024-11-10", "description": "Implemented measurement logging with units"},
    {"date": "2024-11-15", "description": "Created reminder system with notifications"},
    {"date": "2024-11-20", "description": "Built routine management features"},
    {"date": "2024-11-25", "description": "Added trend analysis and summaries"},
    {"date": "2024-11-30", "description": "Implemented data export capabilities"},
]

changelog = generate_changelog(activity_log)
print(changelog)
