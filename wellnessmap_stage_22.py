# === Stage 22: Add favorite records and quick favorite listing ===
# Project: WellnessMap
import json, os

DB = "wellness_map.json"


def load_db():
    if not os.path.exists(DB):
        return {"records": [], "favorites": []}
    with open(DB) as f:
        data = json.load(f)
    return {
        "records": data.get("records", []),
        "favorites": data.get("favorites", {}),  # id -> record_ref
    }


def save_db(db):
    with open(DB, "w") as f:
        json.dump(db, f, indent=2)


def add_favorite(record_id=None, title=""):
    db = load_db()
    if record_id is None and not title.strip():
        print("Need a record ID or non-empty title.")
        return
    fav_id = len(db["favorites"]) + 1
    entry = {"id": fav_id, "title": title, "record_id": record_id}
    db["favorites"].append(entry)
    save_db(db)
    print(f"Favorite #{fav_id}: {entry}")


def list_favorites():
    db = load_db()
    if not db["favorites"]:
        print("No favorites yet.")
        return
    for f in db["favorites"]:
        print(f"{f['id']}. {f.get('title', '')}  (record: {f.get('record_id')})")


def remove_favorite(idx):
    db = load_db()
    if not 0 <= idx < len(db["favorites"]):
        print("Invalid index.")
        return
    removed = db["favorites"].pop(idx)
    save_db(db)
    print(f"Removed favorite #{removed['id']}: {removed.get('title', '')}")


def quick_favorites():
    """Show favs with their latest record summary, if available."""
    db = load_db()
    records = {r["id"]: r for r in db["records"]}
    for f in db["favorites"]:
        rec_id = f.get("record_id")
        title = f.get("title", "")
        ref = rec_id or ""
        print(f"  #{f['id']}  {title}   → record: {ref}")


if __name__ == "__main__":
    # demo usage
    add_favorite(record_id=1, title="Morning stretch")
    add_favorite(title="Hydration reminder", record_id=None)
    list_favorites()
    quick_favorites()
