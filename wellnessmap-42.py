# === Stage 42: Add CSV export without external dependencies ===
# Project: WellnessMap
import csv, json


def export_to_csv(data, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for record in data:
            writer.writerow(record.values())
            return True
