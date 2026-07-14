# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: WellnessMap
import sys, os, json

DRY_RUN = "--dry-run" in sys.argv or "WELLNESSMAP_DRY_RUN" == os.environ.get("WELLNESSMAP_DRY_RUN", "")

def _log(msg):
    print(f"[DRY-RUN] {msg}", file=sys.stderr)

if DRY_RUN:
    for f in ("db.json", "logs/entries.log", "data/metrics.csv"):
        if os.path.exists(f):
            _log(f"  skipping write to {f} (already exists)")
