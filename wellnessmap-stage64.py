# === Stage 64: Add validation for relationship references ===
# Project: WellnessMap
import re

RELATION_PATTERN = re.compile(r"^\s*(\w+)\s*:\s*\[\[(?P<ref>[^\]]+),?\]\]$")


def validate_relationship_references(text: str) -> list[str]:
    """Extract relationship lines and check that each reference is valid."""
    errors = []
    for line in text.splitlines():
        m = RELATION_PATTERN.match(line)
        if not m:
            continue
        ref = m.group("ref").strip()
        # Accept bare word, quoted string, or URL-like token.
        if not (ref.startswith('"') and ref.endswith('"')) and \
               not re.search(r"^[a-zA-Z][\w\-\.]*$", ref):
            errors.append(f"Invalid relationship reference: {line.strip()}")
    return errors
