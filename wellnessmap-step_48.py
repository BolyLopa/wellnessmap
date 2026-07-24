# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: WellnessMap
import unittest
from wellness_map.helpers import create_reminder, validate_symptom_entry


class TestHelpers(unittest.TestCase):
    def test_create_reminder_valid(self):
        entry = {
            "text": "Take vitamins",
            "time": "09:00",
            "recurrence": "daily"
        }
        result = create_reminder(entry)
        self.assertEqual(result["text"], "Take vitamins")
        self.assertEqual(result["time"], "09:00")
        self.assertEqual(result["recurrence"], "daily")

    def test_validate_symptom_entry_valid(self):
        entry = {"symptom": "headache", "intensity": 7, "notes": "after work"}
        result = validate_symptom_entry(entry)
        self.assertTrue(result)

    def test_validate_symptom_entry_invalid_intensity(self):
        entry = {"symptom": "fatigue", "intensity": 15, "notes": ""}
        with self.assertRaises(ValueError):
            validate_symptom_entry(entry)


if __name__ == "__main__":
    unittest.main()
