# === Stage 26: Add weekly summary calculations ===
# Project: WellnessMap
def weekly_summary(records, week_start=None):
    if week_start is None:
        import datetime
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())
    else:
        week_start = datetime.date.fromisoformat(week_start)

    records_in_week = [r for r in records if week_start <= r["date"] < week_start + datetime.timedelta(days=7)]
    if not records_in_week:
        return {"period": f"{week_start.isoformat()}", "count": 0, "measurements": [], "symptoms": []}

    measurements = {}
    symptoms = set()
    for r in records_in_week:
        if r["type"] == "measurement" and r["value"] is not None:
            key = f"{r['metric']}_avg"
            if key not in measurements:
                measurements[key] = []
            measurements[key].append(r["value"])

    summary_measurements = {}
    for k, v in measurements.items():
        summary_measurements[k] = {"avg": sum(v)/len(v), "max": max(v), "min": min(v)}

    return {
        "period": f"{week_start.isoformat()}-{(week_start+datetime.timedelta(days=6)).isoformat()}",
        "count": len(records_in_week),
        "measurements": summary_measurements,
        "symptoms": list(symptoms) if hasattr(symptoms, '__iter__') else []
    }
