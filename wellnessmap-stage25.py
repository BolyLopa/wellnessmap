# === Stage 25: Add daily summary calculations ===
# Project: WellnessMap
def daily_summary(records, date):
    """Compact daily summary from records filtered by date."""
    day = [r for r in records if r.get("date") == date]
    if not day:
        return {"count": 0}
    entries = sum(1 for r in day if r.get("type") == "entry")
    measurements = sum(1 for r in day if r.get("type") == "measurement")
    symptoms = [r["name"] for r in day if r.get("type") == "symptom"]
    return {
        "date": date,
        "entries": entries,
        "measurements": measurements,
        "symptoms": list(set(symptoms)),
        "count": len(day),
    }
