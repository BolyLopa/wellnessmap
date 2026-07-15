# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: WellnessMap
import json, os

def archive_records(records_path="data/records.json", archive_dir="data/archive"):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    with open(records_path) as f:
        records = json.load(f)
    old = [r for r in records if r.get("completed") or r["timestamp"] < "2026-01-01T00:00:00"]
    new = [r for r in records if not (r.get("completed") or r["timestamp"] < "2026-01-01T00:00:00")]
    with open(records_path, "w") as f:
        json.dump(new, f, indent=2)
    for i, rec in enumerate(old):
        safe = "".join(c if c.isalnum() else "_" for c in str(rec.get("id","")))[:16]
        path = os.path.join(archive_dir, f"{safe}.json")
        with open(path, "w") as f:
            json.dump({**rec, "_archived": True}, f, indent=2)
    print(f"Archived {len(old)} record(s), kept {len(new)}.")

def restore_records(records_path="data/records.json", archive_dir="data/archive"):
    if not os.path.exists(archive_dir): return
    archived = sorted([f for f in os.listdir(archive_dir) if f.endswith(".json")])
    restored = []
    with open(records_path) as f:
        current = json.load(f)
    for fname in archived:
        with open(os.path.join(archive_dir, fname)) as f:
            rec = json.load(f)
        if not rec.get("_archived"): continue
        restored.append(rec)
    current.extend(restored)
    with open(records_path, "w") as f:
        json.dump(current, f, indent=2)
    print(f"Restored {len(restored)} record(s).")
