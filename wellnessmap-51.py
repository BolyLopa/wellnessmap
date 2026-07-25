# === Stage 51: Add unit tests for search and filter behavior ===
# Project: WellnessMap
import json, os

WELLNESS_DIR = "wmap_data"


def _load():
    path = os.path.join(WELLNESS_DIR, "routines.json")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        try:
            data = json.load(f)
        except Exception:
            return []
    if isinstance(data, dict) and "entries" in data:
        return [json.loads(e) for e in data["entries"]]
    elif isinstance(data, list):
        return data


def _save(entries):
    path = os.path.join(WELLNESS_DIR, "routines.json")
    with open(path, "w") as f:
        json.dump({"entries": entries}, f)


# --- Unit tests for search and filter behavior ---

def test_search_by_name():
    routines = [
        {"name": "Morning Stretch", "type": "exercise"},
        {"name": "Hydration Check", "type": "measure"},
        {"name": "Evening Wind-Down", "type": "routine"},
    ]
    results = search_routines(routines, "morning")
    assert len(results) == 1
    assert results[0]["name"] == "Morning Stretch"


def test_search_case_insensitive():
    routines = [
        {"name": "Hydration Check", "type": "measure"},
    ]
    results = search_routines(routines, "HYDRATION")
    assert len(results) == 1


def test_filter_by_type():
    routines = [
        {"name": "Morning Stretch", "type": "exercise"},
        {"name": "Hydration Check", "type": "measure"},
        {"name": "Evening Wind-Down", "type": "routine"},
    ]
    exercise_only = filter_routines(routines, "exercise")
    assert len(exercise_only) == 1


def test_search_empty_input():
    routines = [{"name": "A", "type": "x"}]
    results = search_routines(routines, "")
    assert results == []
