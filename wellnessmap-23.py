# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: WellnessMap
def tag_add(tag, record):
    """Add a tag to a wellness record."""
    if "tags" not in record:
        record["tags"] = []
    if tag not in record["tags"]:
        record["tags"].append(tag)
    return record


def tag_remove(tag, record):
    """Remove a tag from a wellness record. Returns False if not present."""
    tags = record.get("tags", [])
    if tag in tags:
        tags.remove(tag)
        record["tags"] = tags
        return True
    return False


def summarize_by_tag(records, tag):
    """Return records that contain the given tag, as a new list."""
    return [r for r in records if tag in r.get("tags", [])]
