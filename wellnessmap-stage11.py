# === Stage 11: Add JSON export for the current application state ===
# Project: WellnessMap
def export_state_to_json(state):
    """Export the current application state to a compact JSON string."""
    import json
    serializable = {}
    for key, value in state.items():
        if isinstance(value, dict) and "db" in value:
            db = value["db"]
            value = {k: v for k, v in db.items() if k != "db"}
        serializable[key] = value
    return json.dumps(serializable, indent=2)
