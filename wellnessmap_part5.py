# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: WellnessMap
def update_record(db, record_id, field, value):
    """Update a single field of an existing record, returning False if missing."""
    try:
        cursor = db.cursor()
        cursor.execute(f"UPDATE records SET {field}=%s WHERE id=%s", (value, record_id))
        updated = cursor.rowcount > 0
        if not updated and field == "id":
            raise ValueError("Cannot update the primary key")
        return updated
    except Exception:
        db.rollback()
        return False

def upsert_record(db, table_name, fields):
    """Insert or update a record. Returns the final id."""
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO {table_name} ({', '.join(fields.keys())}) VALUES ({', '.join(['%s'] * len(fields))})", tuple(fields.values()))
    db.commit()
    return cursor.lastrowid

def clear_records(db, table_name):
    """Remove all records from a given table."""
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    db.commit()
