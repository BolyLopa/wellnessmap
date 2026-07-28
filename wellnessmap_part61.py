# === Stage 61: Add performance timing for core list and search operations ===
# Project: WellnessMap
import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        return result, elapsed_ms
    return wrapper

def benchmark_list_ops():
    import random
    data = [random.random() for _ in range(500)]

    @timed
    def linear_search(lst, target):
        for i, v in enumerate(lst):
            if v == target:
                return i, 0
        return -1, 0

    @timed
    def binary_search_sorted(lst, target):
        lst_s = sorted(lst)
        lo, hi = 0, len(lst_s) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if lst_s[mid] == target:
                return mid, 1
            elif lst_s[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1, 0

    @timed
    def filter_above(lst, threshold):
        return [x for x in lst if x > threshold], 2

    @timed
    def map_values(lst, factor):
        return [x * factor for x in lst], 3

    @timed
    def count_occurrences(lst, target):
        c = 0
        for v in lst:
            if v == target:
                c += 1
        return c, 4

    results = {
        "linear_search": linear_search(data, random.random()),
        "binary_search_sorted": binary_search_sorted(data, random.random()),
        "filter_above": filter_above(data, 0.5),
        "map_values": map_values(data, 2),
        "count_occurrences": count_occurrences(data, data[0]),
    }

    for name, (val, ms) in results.items():
        print(f"{name}: result={val}, elapsed={ms:.3f}ms")
