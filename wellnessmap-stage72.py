# === Stage 72: Add Markdown report export ===
# Project: WellnessMap
def export_to_markdown(wellness_data, output_path="wellness_report.md"):
    """Generate a Markdown wellness report from structured data."""
    with open(output_path, "w") as f:
        f.write("# WellnessMap Report\n\n")
        if "routines" in wellness_data:
            f.write("## Routines\n")
            for routine in wellness_data["routines"]:
                f.write(f"- **{routine.get('name', 'Unknown')}** ({' '.join(routine.get('schedule', []))})\n")
        if "symptoms" in wellness_data:
            f.write("\n## Symptoms\n")
            for symptom in wellness_data["symptoms"]:
                f.write(f"- **{symptom.get('name', 'Unknown')}** - {symptom.get('severity', 'N/A')}\n")
        if "measurements" in wellness_data:
            f.write("\n## Measurements\n")
            for m in wellness_data["measurements"]:
                f.write(f"- **{m.get('metric', 'N/A')}**: {m.get('value', 'N/A')}\n")
        if "reminders" in wellness_data:
            f.write("\n## Reminders\n")
            for reminder in wellness_data["reminders"]:
                f.write(f"- [{reminder.get('status', 'pending')}] **{reminder.get('text', 'No text')}**\n")
        if "trends" in wellness_data:
            f.write("\n## Trends\n")
            for trend_key, trend_value in wellness_data["trends"].items():
                f.write(f"- {trend_key}: {trend_value}\n")
    print(f"Report exported to {output_path}")
