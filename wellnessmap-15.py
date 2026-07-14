# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: WellnessMap
def dispatch(text):
    text = text.strip().lower()
    if text.startswith("status"):
        return {"type": "status", "data": get_status()}
    if text.startswith("add symptom") or text.startswith("log symptom"):
        parts = text.split(maxsplit=1)
        name = parts[1] if len(parts) > 1 else "general"
        return {"type": "symptom_added", "data": {"name": name}}
    if text.startswith("add measurement") or text.startswith("log measurement"):
        parts = text.split(maxsplit=2)
        unit = parts[2] if len(parts) > 2 else ""
        return {"type": "measurement_added", "data": {"unit": unit}}
    if text.startswith("schedule reminder"):
        parts = text.split(maxsplit=1)
        note = parts[1] if len(parts) > 1 else "check-in"
        return {"type": "reminder_scheduled", "data": {"note": note}}
    if text == "help":
        return {
            "type": "help",
            "data": [
                "status",
                "add symptom <name>",
                "log measurement <unit>",
                "schedule reminder <note>",
                "help"
            ]
        }
    if text == "quit":
        return {"type": "quit"}
    return {"type": "unknown", "data": {"input": text}}
