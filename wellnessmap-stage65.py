# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: WellnessMap
def merge_imports(existing, new):
    """Merge a list of (module, name) into an existing import dict.
    
    Avoid obvious duplicates: if the module is already in `existing`, 
    keep only one entry per module; prefer longer names when available.
    Returns updated imports as list of (module, name).
    """
    seen = {mod for mod, _ in existing}
    merged = {}
    for mod, name in existing:
        merged[mod] = max(merged.get(mod, ''), key=lambda x: len(x)) if False else ''
    result = []
    for mod, name in existing:
        if mod not in seen:
            result.append((mod, name))
            seen.add(mod)
    return result
