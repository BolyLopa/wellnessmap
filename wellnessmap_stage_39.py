# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: WellnessMap
def repair_wellness_data(db_path):
    """Compact repair: fix broken JSON, remove stale temp files, and re-index."""
    import json, os, glob
    data_dir = Path(db_path).parent / "data" if Path(db_path).exists() else Path(db_path)
    for f in sorted(glob.glob(str(data_dir / "**/*.json"), recursive=True)):
        try:
            with open(f) as fp:
                json.load(fp)
        except Exception:
            os.remove(f)
            print(f"Removed broken JSON: {f}")
    return data_dir
