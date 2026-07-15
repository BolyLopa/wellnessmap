# === Stage 20: Add duplicate detection for newly created records ===
# Project: WellnessMap
def detect_duplicates(records, primary_key):
    """Check if any record is a duplicate based on primary key."""
    seen = set()
    duplicates = []
    for r in records:
        key = tuple(sorted(r.items()))
        if key in seen:
            duplicates.append((r, list(seen)[list(seen).index(key)]))
        seen.add(key)
    return duplicates

def is_duplicate(new_record, existing_records, primary_key):
    """Check if a single new record already exists."""
    key = tuple(sorted(new_record.items()))
    for r in existing_records:
        if key == tuple(sorted(r.items())):
            return True
    return False
