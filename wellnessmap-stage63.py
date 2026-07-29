# === Stage 63: Add relationships between records where useful ===
# Project: WellnessMap
# Step 63: Add relationships between records where useful
def link_records(records):
    """Establish meaningful links between wellness records of different types."""
    linked = []
    for i, record in enumerate(records):
        if isinstance(record, RoutineRecord) and hasattr(record, 'routine_id'):
            related = [r for r in records if hasattr(r, 'routine_id') and r.routine_id == record.routine_id]
            linked.append({"record": record, "related_records": related})
    return linked
