# === Stage 43: Add CSV import for the primary record type ===
# Project: WellnessMap
import csv
from datetime import date, time


def load_records(filename):
    """Load WellnessMap records from a CSV file.

    Expected columns: type, description, value, unit, timestamp (YYYY-MM-DD HH:MM).
    Returns a list of dicts ready for use as primary record data."""
    records = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = row.get('timestamp', '')
            if len(ts) >= 10:
                date_part = ts[:10]
                time_part = ts[10:]
                try:
                    rec_date = date.fromisoformat(date_part)
                except ValueError:
                    rec_date = None
            else:
                rec_date = None

            records.append({
                'type': row.get('type', ''),
                'description': row.get('description', ''),
                'value': float(row['value']) if row.get('value', '').strip() else 0.0,
                'unit': row.get('unit', ''),
                'timestamp': ts.strip(),
                'date': rec_date,
            })
    return records


if __name__ == '__main__':
    sample = [
        {'type': 'measurement', 'description': 'Blood Pressure', 'value': 120, 'unit': 'mmHg', 'timestamp': '2024-03-15 09:30'},
        {'type': 'symptom', 'description': 'Headache', 'value': 7, 'unit': '', 'timestamp': '2024-03-15 10:00'},
    ]

    import io
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=['type', 'description', 'value', 'unit', 'timestamp'])
    writer.writeheader()
    for r in sample:
        writer.writerow(r)

    loaded = load_records(buf.name)
    for rec in loaded:
        print(f"{rec['type']:12s} | {rec['description']} | value={rec['value']:.0f} {rec['unit']}")
