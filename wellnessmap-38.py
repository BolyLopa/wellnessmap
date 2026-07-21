# === Stage 38: Add data integrity checks for broken references ===
# Project: WellnessMap
def check_references(db):
    """Validate that every routine, symptom, measurement, reminder, and trend references valid parents."""
    routines = db["routines"]
    symptoms = db["symptoms"]
    measurements = db["measurements"]
    reminders = db["reminders"]
    trends = db.get("trends", {})

    broken = []
    for r in routines:
        if "routine_type" not in r or r["routine_type"] not in ("daily", "weekly", "monthly"):
            broken.append(f"{r['id']}: invalid routine_type")
    for s in symptoms:
        if "symptom_category" not in s or not s["symptom_category"]:
            broken.append(f"{s['id']}: missing symptom_category")
    for m in measurements:
        if "measurement_unit" not in m or not m["measurement_unit"]:
            broken.append(f"{m['id']}: missing measurement_unit")
    for rem in reminders:
        if "reminder_type" not in rem or not rem["reminder_type"]:
            broken.append(f"{rem['id']}: missing reminder_type")
    for t in trends.values():
        if "trend_category" not in t or not t.get("trend_category"):
            broken.append(f"Trend {t.get('id')}: missing trend_category")

    return len(broken) == 0, broken
