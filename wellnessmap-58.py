# === Stage 58: Add bulk update behavior for selected records ===
# Project: WellnessMap
def bulk_update_records(records, updates_by_id):
    """Update multiple records in one call using a dict of {id: updated_fields}."""
    if not records:
        return []
    for rec in records:
        rid = rec.get("id") or rec.get("_id")
        if rid and rid in updates_by_id:
            rec.update(updates_by_id[rid])
    return records

def bulk_delete_records(records, ids_to_remove):
    """Remove matching records from a list by their ids."""
    id_set = set(ids_to_remove)
    return [r for r in records if not (r.get("id") or r.get("_id")) in id_set]

def bulk_merge_reminders(existing, incoming):
    """Merge two reminder lists: keep existing unless an incoming entry matches by title+date."""
    kept = []
    for ex in existing:
        skip = any(
            (i.get("title") or "") == (ex.get("title") or "")
            and i.get("scheduled_date") == ex.get("scheduled_date")
            and i.get("reminder_type") == ex.get("reminder_type")
            for i in incoming
        )
        if not skip:
            kept.append(ex)
    return kept + [i for i in incoming if i.get("status") != "completed"]
