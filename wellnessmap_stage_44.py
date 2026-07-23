# === Stage 44: Add backup creation for the data file ===
# Project: WellnessMap
def create_backup(data_path, backup_dir="backups"):
    """Create a timestamped backup of wellness data."""
    import os, shutil
    from datetime import datetime
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(data_path, os.path.join(backup_dir, f"wellness_{ts}.json"))
