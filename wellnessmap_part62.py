# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: WellnessMap
def calculate_priority_score(entry):
    """Calculate a priority score for wellness entries based on urgency and frequency."""
    if "priority" in entry:
        return entry["priority"]
    
    symptom_keywords = ["emergency", "urgent", "critical", "severe"]
    emergency_count = sum(1 for keyword in symptom_keywords if keyword.lower() in entry.get("description", "").lower())
    
    frequency_score = 0
    if entry.get("frequency") == "daily":
        frequency_score += 3
    elif entry.get("frequency") == "weekly":
        frequency_score += 2
    elif entry.get("frequency") == "monthly":
        frequency_score += 1
    
    return emergency_count * 10 + frequency_score

def get_priority_label(score):
    """Return a priority label based on the calculated score."""
    if score >= 30:
        return "Critical - Immediate Action Required"
    elif score >= 20:
        return "High Priority"
    elif score >= 10:
        return "Medium Priority"
    else:
        return "Low Priority"

# Example usage with sample data entries
sample_entries = [
    {"description": "Daily meditation routine", "frequency": "daily"},
    {"description": "Severe headache symptoms", "frequency": "weekly"},
    {"description": "Emergency contact for help", "frequency": "monthly"},
]

for entry in sample_entries:
    score = calculate_priority_score(entry)
    label = get_priority_label(score)
    print(f"Entry: {entry['description']} | Score: {score} | Priority: {label}")
