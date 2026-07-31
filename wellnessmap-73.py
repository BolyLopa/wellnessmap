# === Stage 73: Add a lightweight HTML report export ===
# Project: WellnessMap
import json, os
from datetime import date

def export_report(data_path="wellness_map.json", output_path="report.html"):
    with open(data_path) as f:
        data = json.load(f)
    routines = data.get("routines", [])
    measurements = [m for m in data.get("measurements", []) if "date" in m]
    reminders = [r for r in data.get("reminders", []) if "due_date" in r and r["completed"]]
    rows = []
    for r in routines:
        rows.append(f"<tr><td>{r['name']}</td><td>{r['schedule']}</td><td>{len(r.get('measurements',[]))}</td></tr>")
    for m in measurements[-10:]:
        rows.append(f"<tr><td>{m.get('metric','?')} {m.get('value','')}</td><td>{m['date']}</td></tr>")
    rows_str = "\n".join(rows)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>WellnessMap Report</title>
<style>body{{font-family:sans-serif;margin:2em}}table{{border-collapse:collapse;width:100%%}}th,td{{padding:.5em;border:1px solid #ccc;text-align:left}}</style>
</head><body><h1>WellnessMap Report — {date.today().strftime('%%Y-%%m-%%d')}</h1>
<p>Routines: {len(routines)} | Measurements shown: {min(len(measurements),10)}</p>
<table><tr><th>Metric/Name</th><th>Date/Schedule</th><th>Count</th></tr>{rows_str}</table>
<hr><p>Completed reminders: {len(reminders)}</p></body></html>"""
    with open(output_path, "w") as f:
        f.write(html)
    print(f"Report saved to {output_path}")
