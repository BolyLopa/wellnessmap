# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: WellnessMap
def compare_snapshot(before, after):
    """Compare two wellness data snapshots and return a summary of changes."""
    if before is None:
        return {"status": "new", "changes": {}}
    
    changes = {}
    
    for key in set(list(before.keys()) + list(after.keys())):
        old_val = before.get(key)
        new_val = after.get(key)
        
        if old_val == new_val:
            continue
        
        # Handle numeric values
        try:
            change = new_val - old_val
            changes[key] = {
                "old": old_val,
                "new": new_val,
                "change": change,
                "direction": "improved" if isinstance(old_val, (int, float)) and isinstance(new_val, (int, float)) else None
            }
        except TypeError:
            changes[key] = {"old": old_val, "new": new_val}
    
    return {"status": "changed", "changes": changes}
