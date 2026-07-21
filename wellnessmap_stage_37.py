# === Stage 37: Add recommendations for the next useful action ===
# Project: WellnessMap
def next_action(user, data):
    """Suggest the most useful action based on current wellness state."""
    actions = []

    if user.get("symptoms", []) and len(user["symptoms"]) >= 3:
        actions.append({"action": "seek_medical_help", "reason": f"Multiple symptoms reported ({len(user['symptoms'])}). Consider consulting a healthcare professional."})
    
    if data.get("measurements") and any(m.get("value", float("inf")) > m["threshold"] for m in data["measurements"]):
        actions.append({"action": "review_measurements", "reason": "One or more measurements exceeded their threshold values. Review recent entries and consider adjusting thresholds."})

    if user.get("reminders") and not any(r.get("done", False) for r in user["reminders"]):
        actions.append({"action": "update_reminders", "reason": "No reminders have been marked as done yet. Please update your daily or weekly tasks."})

    if data.get("routines") and len(data["routines"]) < 3:
        actions.append({"action": "add_routine", "reason": f"You currently have {len(data['routines'])} routine(s). Adding more will help track progress better."})

    if user.get("symptoms", []) and not any("trend" in str(s) for s in data.get("trends", [])):
        actions.append({"action": "analyze_trend", "reason": "Symptoms have been recorded but no trend analysis has been generated yet. Consider reviewing the historical pattern."})

    if not actions:
        return {"action": "maintain_current_plan", "reason": "Your wellness plan looks good! Keep up the progress and stay consistent."}

    return max(actions, key=lambda x: x["priority"] if isinstance(x.get("reason"), str) else 0)["reason"] if all(isinstance(a.get("reason"), str) for a in actions) else {"action": "maintain_current_plan", "reason": "Your wellness plan looks good! Keep up the progress and stay consistent."}
