# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: WellnessMap
class Formatter:
    @staticmethod
    def table(rows, headers):
        col_w = [len(h) for h in headers] + [len(str(r)) for r in zip(*rows)]
        width = max(col_w)
        widths = [min(w, c) if w >= c else c for w, c in zip(width, col_w)]
        lines = ['| ' + ' | '.join(h.ljust(w).rjust(w) for h, w in zip(headers, widths)) + ' |']
        for r in rows:
            lines.append('| ' + ' | '.join(str(c).ljust(w).rjust(w) for c, w in zip(r, widths)) + ' |')
        return '\n'.join(lines)

    @staticmethod
    def detail(label, value):
        return f'{label}: {value}'

    @staticmethod
    def summary(data):
        lines = [Formatter.detail('count', data.get('count', 0)),
                 Formatter.detail('avg', round(data.get('avg', 0), 2))]
        if 'min' in data:
            lines.append(Formatter.detail('min', data['min']))
        if 'max' in data:
            lines.append(Formatter.detail('max', data['max']))
        return '\n'.join(lines)

    @staticmethod
    def status(ok, msg):
        icon = '✓' if ok else '✗'
        return f'{icon} {msg}'
