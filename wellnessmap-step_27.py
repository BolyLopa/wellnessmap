# === Stage 27: Add monthly summary calculations ===
# Project: WellnessMap
from datetime import date, timedelta


def monthly_summary(records):
    """Group records by month and return a dict keyed by YYYY-MM."""
    groups = {}
    for r in records:
        key = r["date"].strftime("%Y-%m")
        if key not in groups:
            groups[key] = []
        groups[key].append(r)
    return groups


def compute_trend(records):
    """Simple linear trend over time (slope) from a list of records."""
    if len(records) < 2:
        return None
    n = float(len(records))
    x_vals = [float(i) for i in range(n)]
    y_vals = [r["value"] for r in sorted(records, key=lambda r: r["date"])]
    mean_x = sum(x_vals) / n
    mean_y = sum(y_vals) / n
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    denominator = sum((x - mean_x) ** 2 for x in x_vals)
    if denominator == 0:
        return None
    slope = numerator / denominator
    return round(slope, 3)


def monthly_trend_summary(records):
    """Return {YYYY-MM: {'count': int, 'avg': float, 'trend_slope': float}}."""
    groups = monthly_summary(records)
    result = {}
    for month_key in sorted(groups.keys()):
        month_records = groups[month_key]
        values = [r["value"] for r in month_records]
        avg_val = round(sum(values) / len(values), 2) if values else None
        trend_slope = compute_trend(month_records)
        result[month_key] = {
            "count": len(month_records),
            "avg": avg_val,
            "trend_slope": trend_slope,
        }
    return result


# Example usage:
if __name__ == "__main__":
    sample_records = [
        {"date": date(2024, 1, 5), "value": 7.5},
        {"date": date(2024, 1, 15), "value": 8.0},
        {"date": date(2024, 1, 25), "value": 7.8},
        {"date": date(2024, 2, 10), "value": 9.1},
        {"date": date(2024, 2, 20), "value": 9.3},
    ]
    print(monthly_trend_summary(sample_records))
