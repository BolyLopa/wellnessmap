# === Stage 46: Add a schema version field and migration helper ===
# Project: WellnessMap
SCHEMA_VERSION = 1


def migrate_database(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys=ON")
    try:
        if SCHEMA_VERSION >= 2:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY)"
            )
            cur.execute("INSERT OR IGNORE INTO schema_migrations VALUES (?)", (SCHEMA_VERSION,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Migration error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    migrate_database("wellness_map.db")
