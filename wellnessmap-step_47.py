# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: WellnessMap
import json, os
from datetime import date, timedelta
from wellness_map.models import Routine, Symptom, Measurement, Reminder, WellnessMap


def demo_scenario():
    map = WellnessMap("Alice")

    routine = Routine("Morning", "08:00", ["Hydrate", "Stretch"])
    symptom = Symptom("Headache", severity=3)
    measurement = Measurement("HeartRate", 72, bpm=True)
    reminder = Reminder("Take vitamins", "09:00")

    map.add(routine).add(symptom).add(measurement).add(reminder)
    today = date.today()
    yesterday = today - timedelta(days=1)
    week_ago = today - timedelta(days=7)
    map.measurements.append(Measurement("Sleep", 6.5, hours=True))
    map.measurements.append(Measurement("Sleep", 7.0, hours=True, date=yesterday))
    map.measurements.append(Measurement("Sleep", 5.8, hours=True, date=week_ago))

    trend = map.trend_summary()
    print(f"Today: {map.name}, routines={len(map.routines)}, symptoms={len(map.symptoms)}")
    print(f"Trend — Sleep (hrs): {trend}")


if __name__ == "__main__":
    demo_scenario()
