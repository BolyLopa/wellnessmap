# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: WellnessMap
import datetime


def parse_date(value, fmt=None):
    """Parse a date string and return a datetime.date object."""
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        for candidate in (fmt or "%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y", "%Y/%m/%d"):
            try:
                return datetime.datetime.strptime(value.strip(), candidate).date()
            except ValueError:
                continue
        raise ValueError(f"Unrecognized date string: '{value}' (supported formats: {fmt or '%Y-%m-%d'})")
    if isinstance(value, datetime.datetime):
        return value.date()
    raise TypeError(f"Unsupported type for date parsing: {type(value).__name__}")


def parse_datetime(value, fmt=None):
    """Parse a datetime string and return a datetime object."""
    if isinstance(value, datetime.datetime):
        return value
    if isinstance(value, str):
        for candidate in (fmt or "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y %I:%M %p"):
            try:
                return datetime.datetime.strptime(value.strip(), candidate)
            except ValueError:
                continue
        raise ValueError(f"Unrecognized datetime string: '{value}' (supported formats: {fmt or '%Y-%m-%d %H:%M'})")
    if isinstance(value, datetime.date):
        return value.replace(hour=0, minute=0, second=0)
    raise TypeError(f"Unsupported type for datetime parsing: {type(value).__name__}")


def today():
    """Return the current date as a plain datetime.date."""
    return datetime.date.today()
