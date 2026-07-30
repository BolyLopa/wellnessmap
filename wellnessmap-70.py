# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: WellnessMap
CLEAR_STATE = "clear_state"

def clear_state_command(state, confirmation_flag):
    """Clear wellness map state after user confirms."""
    if not confirmation_flag:
        raise ValueError("Confirmation required to clear state")
    return {
        "state": {},
        "actions_history": [],
        "summary": None,
        "clear_at": time.time(),
        "message": "WellnessMap state cleared successfully."
    }
