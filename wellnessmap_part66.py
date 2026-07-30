# === Stage 66: Add export of a short status dashboard ===
# Project: WellnessMap
def export_dashboard(records, routines):
    """Export a short status dashboard from wellness records and routines."""
    if not records:
        return "No records found."
    latest = max(r["date"] for r in records)
    lines = [f"=== Wellness Status Dashboard (as of {latest}) ===", f"Total records: {len(records)}"]
    symptom_counts = {}
    measurement_units = set()
    reminder_count = 0
    for rec in records:
        if "symptom" in rec:
            sym = rec["symptom"].lower()
            symptom_counts[sym] = symptom_counts.get(sym, 0) + 1
        if "measurement" in rec and "unit" in rec["measurement"]:
            measurement_units.add(rec["measurement"]["unit"])
        if "reminder" in rec:
            reminder_count += 1
    lines.append(f"\nTop Symptoms:")
    for sym, cnt in sorted(symptom_counts.items(), key=lambda x: -x[1]):
        lines.append(f"  {sym}: {cnt} occurrence(s)")
    lines.append(f"\nReminder count: {reminder_count}")
    if measurement_units:
        lines.append(f"Measurement units used: {', '.join(sorted(measurement_units))}")
    return "\n".join(lines)
