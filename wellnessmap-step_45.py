# === Stage 45: Add restore from backup with validation ===
# Project: WellnessMap
import os, json, datetime

BACKUP_FILE = "wellness_backup.json"
DATA_FILES = ["routines.json", "symptoms.json", "measurements.json", "reminders.json"]


def validate_data(data_files):
    errors = []
    for f in data_files:
        if not os.path.exists(f):
            errors.append(f"{f} is missing")
        else:
            try:
                with open(f, "r") as fp:
                    json.load(fp)
            except Exception as e:
                errors.append(f"Invalid JSON in {f}: {e}")
    return errors


def restore_from_backup():
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return False

    with open(BACKUP_FILE, "r") as fp:
        backup = json.load(fp)

    errors = validate_data(DATA_FILES)
    if errors:
        print(f"Backup validation failed:\n  - {'; '.join(errors)}\nAborting restore.")
        return False

    for f in DATA_FILES:
        with open(f, "w") as fp:
            json.dump(backup[f], fp, indent=2)

    os.remove(BACKUP_FILE)
    print("Restore from backup completed successfully.")
    return True
