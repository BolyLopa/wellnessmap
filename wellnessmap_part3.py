# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: WellnessMap
# wellness_validation.py – compact validation helpers for WellnessMap models
import re


def is_valid_id(value, prefix="id"):
    """Return True if *value* looks like a well-formed identifier."""
    return bool(re.fullmatch(rf"[a-zA-Z_][\w.]*-{prefix}[-\w]+", value))


def is_non_empty_text(value):
    """Reject empty strings and pure whitespace."""
    return isinstance(value, str) and len(value.strip()) > 0


def validate_required_fields(kwargs):
    """Raise ValueError when any required key in *kwargs* is missing or falsy."""
    required = ["name", "description"]
    for field in required:
        val = kwargs.get(field)
        if not val or not isinstance(val, str) or len(val.strip()) == 0:
            raise ValueError(f"Missing or empty required field: {field}")
