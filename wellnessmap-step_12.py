# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: WellnessMap
import json


def load_wellness_data(path: str) -> dict | list:
    """Load wellness data from JSON, returning friendly error messages for malformed files."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            raw = f.read()
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")

    if not raw.strip():
        return {}

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        line_no = str(exc.lineno).strip() or "?"
        col_no = str(exc.colno).strip() or "?"
        bad_snippet = raw[max(0, exc.pos - 20):exc.pos + 20]
        raise ValueError(
            f"Malformed JSON at line {line_no}, column {col_no}:\n"
            f"  '{bad_snippet}'\n"
            f"  Suggested fix: check for missing commas, unquoted keys, or trailing punctuation."
        )

    if isinstance(data, dict):
        return data
    if isinstance(data, list):
        return data
    raise ValueError(f"JSON root must be object or array, got {type(data).__name__}")
