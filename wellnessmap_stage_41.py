# === Stage 41: Add plain text import for a simple line-based format ===
# Project: WellnessMap
def load_line_text(path):
    """Load a simple line-based text format: each non-empty line is a record."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";", maxsplit=2)
            if len(parts) >= 3:
                record = {
                    "id": int(parts[0].strip()),
                    "label": parts[1].strip(),
                    "value": parts[2].strip(),
                }
                records.append(record)
    return records

def dump_line_text(records, path):
    """Write records in the same line-based format."""
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(f"{r['id']};{r['label']};{r['value']}\n")

if __name__ == "__main__":
    samples = load_line_text("samples.txt")
    print(samples)
