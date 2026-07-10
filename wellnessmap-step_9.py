# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: WellnessMap
def sort_wellness_items(items, key_fn=None):
    """Sort wellness items by title, date, priority, or last update time."""
    if key_fn is None:
        return sorted(items)
    return sorted(items, key=key_fn)
