# === Stage 32: Add pagination helpers for long console output ===
# Project: WellnessMap
import math


def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def paginated_print(items, per_page=12, header=None, footer=None):
    if header:
        print(header)
    if not items:
        return
    total = len(items)
    for idx, chunk in enumerate(chunk_list(items, per_page), 1):
        for item in chunk:
            print(item)
        if idx < math.ceil(total / per_page):
            print(f"--- Page {idx}/{math.ceil(total / per_page)} ---")
    if footer:
        print(footer)
