# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: WellnessMap
import unittest
from wellness_map.data_store import DataStore


class TestDataStore(unittest.TestCase):
    def setUp(self):
        self.ds = DataStore()
        self.ds.insert("routine", {"id": 1, "name": "morning"})

    def test_update_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.ds.update("routine", {"id": 99})

    def test_delete_nonexistent_key(self):
        keys = self.ds.keys()
        self.assertNotIn(99, keys)
