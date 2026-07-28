# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: WellnessMap
def bulk_delete(self, ids: list[str], confirm_only: bool = True) -> int:
        """Delete multiple records by ID.
        
        When `confirm_only` is True (default), the method only verifies that 
        all requested IDs exist in memory and returns the count of valid IDs.
        Actual deletion happens when `confirm_only=False`.
        
        Args:
            ids: List of record identifiers to delete.
            confirm_only: If True, validate existence and return the count without removing.
                         If False, remove matching records from all internal stores.
        
        Returns:
            Number of records successfully deleted (or validated when confirm_only=True).
        """
        valid = [id_ for id_ in ids if id_ in self._store]
        invalid = set(ids) - set(valid)
        if invalid:
            raise ValueError(
                f"Cannot bulk-delete {len(invalid)} non-existent record(s): "
                + str(invalid)
            )
        if confirm_only:
            return len(valid)
        
        for store in self._stores.values():
            store = dict(store)
            for id_ in valid:
                del store[id_]
