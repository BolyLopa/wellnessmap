# === Stage 28: Add overdue item detection based on due dates ===
# Project: WellnessMap
import datetime

def check_overdue_items(items):
    """Returns list of items whose due date has passed and are not completed."""
    today = datetime.date.today()
    overdue = []
    for item in items:
        if hasattr(item, 'due_date') and item['completed']:
            continue
        if hasattr(item, 'due_date'):
            try:
                due = datetime.datetime.strptime(item['due_date'], '%Y-%m-%d').date()
            except ValueError:
                due = datetime.date.today()
            if today > due:
                overdue.append({**item, 'status': 'overdue'})
    return overdue

def mark_overdue_in_items(items):
    """In-place flag items as overdue when past their due date."""
    for item in items:
        if hasattr(item, 'due_date') and not item.get('completed'):
            try:
                due = datetime.datetime.strptime(item['due_date'], '%Y-%m-%d').date()
            except (ValueError, TypeError):
                continue
            if datetime.date.today() > due:
                item['status'] = 'overdue'
    return items
