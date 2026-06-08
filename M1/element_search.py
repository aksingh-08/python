def linear_search_analyzed(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1
import time, random
n = 1_000_000
data = list(range(n))
start = time.perf_counter()
linear_search_analyzed(data, 0)
best_case = time.perf_counter() - start