# === Stage 31: Add compact table rendering for long lists ===
# Project: WellnessMap
def render_compact_table(headers, rows):
    """Render a compact table for long lists."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    lines = []
    sep = '  '.join('-' * w for w in col_widths)
    lines.append(sep)
    header_line = '  '.join(h.ljust(w) for h, w in zip(headers, col_widths))
    lines.append(header_line)
    lines.append(sep)
    for row in rows:
        line = '  '.join(str(v).ljust(w) for v, w in zip(row, col_widths))
        lines.append(line)

    return '\n'.join(lines)
