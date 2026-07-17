# === Stage 24: Add grouped summaries by category or status ===
# Project: WellnessMap
def grouped_summaries(records, group_by=None):
    """Group wellness records by category/status and return compact summaries."""
    if group_by is None:
        group_by = lambda r: "Other"
    from collections import defaultdict
    groups = defaultdict(list)
    for rec in records:
        key = group_by(rec) if callable(group_by) else rec.get(group_by, "Unknown")
        groups[key].append(rec)

    summaries = []
    for key, items in sorted(groups.items()):
        counts = {status: sum(1 for i in items if i.get("status") == status)
                  for status in ("normal", "warning", "critical")}
        measurements = [i.get("measurement_value") for i in items if i.get("measurement_value")]
        avg_val = (sum(measurements) / len(measurements)) if measurements else None
        summaries.append({
            "category": key,
            "count": len(items),
            "status_counts": counts,
            "avg_measurement": round(avg_val, 2) if avg_val is not None else None,
        })
    return summaries


if __name__ == "__main__":
    sample = [
        {"category": "sleep", "status": "normal", "measurement_value": 7.5},
        {"category": "sleep", "status": "warning", "measurement_value": 6.0},
        {"category": "hydration", "status": "normal", "measurement_value": 2.1},
        {"category": "mood", "status": "normal", "measurement_value": None},
    ]
    print(grouped_summaries(sample))
