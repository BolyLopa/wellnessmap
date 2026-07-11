# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: WellnessMap
def case_insensitive_search(text, query):
    """Case-insensitive search across multiple wellness fields."""
    query_lower = query.lower()
    if any(query_lower in text.lower().split() for _ in range(1)):
        return True
    return False
