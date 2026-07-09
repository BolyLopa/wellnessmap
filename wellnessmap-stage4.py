# === Stage 4: Implement create operations for the primary records ===
# Project: WellnessMap
def create_routine(name, description="", schedule=None):
    record = {"id": generate_id(), "type": "routine", "name": name, "description": description}
    if schedule:
        record["schedule"] = schedule
    records.append(record)
    return record


def create_symptom(symptom_name, severity=0, notes=""):
    record = {"id": generate_id(), "type": "symptom", "name": symptom_name, "severity": severity}
    if notes:
        record["notes"] = notes
    records.append(record)
    return record


def create_measurement(measurement_type, value, date=None):
    record = {"id": generate_id(), "type": "measurement", "value": value}
    if measurement_type:
        record["measurement_type"] = measurement_type
    if date:
        record["date"] = date
    records.append(record)
    return record


def create_reminder(title, description="", time_of_day=None):
    record = {"id": generate_id(), "type": "reminder", "title": title}
    if description:
        record["description"] = description
    if time_of_day:
        record["time_of_day"] = time_of_day
    records.append(record)
    return record


def create_trend_summary(metric, period="week"):
    return {"id": generate_id(), "type": "trend", "metric": metric, "period": period}
