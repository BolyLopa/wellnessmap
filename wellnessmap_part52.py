# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: WellnessMap
def get_routine_status(routine):
    """Return a human-readable status string for any routine object."""
    if isinstance(routine, Routine):
        return f"{routine.name}: {'active' if routine.active else 'inactive'}"
    if isinstance(routine, DailyRoutine):
        return (f"{routine.name} (daily) - last done: {routine.last_done}"
                if routine.last_done else f"{routine.name} (daily) - never done")
    if isinstance(routine, Reminder):
        return f"{routine.text}: due in {int(routine.interval / 60)} min"
    return str(routine)


def calculate_trend(measurements_list):
    """Return a simple trend label based on the latest values."""
    if len(measurements_list) < 2:
        return "insufficient data"
    recent = [m.value for m in measurements_list[-5:]]
    avg_recent = sum(recent) / len(recent)
    avg_all = sum(m.value for m in measurements_list) / len(measurements_list)
    if abs(avg_recent - avg_all) < 0.1 * avg_all:
        return "stable"
    elif avg_recent > avg_all:
        return "improving"
    else:
        return "declining"


def summarize_day(day_measurements):
    """Return a compact summary string for all measurements of one day."""
    if not day_measurements:
        return "no data today"
    values = [m.value for m in day_measurements]
    min_v, max_v = min(values), max(values)
    return f"{day_measurements[0].name}: {min_v:.1f}-{max_v:.1f}"
