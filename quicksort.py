import random
import time
import statistics

# -----------------------------
# 1️⃣ Deterministic QuickSort (fixed pivot = last element)
# -----------------------------
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Fixed pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)


# -----------------------------
# 2️⃣ Randomized QuickSort (pivot chosen randomly)
# -----------------------------
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# -----------------------------
# 3️⃣ Helper: measure execution time
# -----------------------------
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]
    trials = 5

    print("---- Randomized vs Deterministic QuickSort ----\n")

    for n in sizes:
        det_times = []
        rand_times = []

        for _ in range(trials):
            arr = [random.randint(1, 10000) for _ in range(n)]
            det_times.append(measure_time(deterministic_quicksort, arr))
            rand_times.append(measure_time(randomized_quicksort, arr))

        print(f"Array Size: {n}")
        print(f"  Deterministic QuickSort Avg Time: {statistics.mean(det_times):.6f} sec")
        print(f"  Randomized QuickSort Avg Time   : {statistics.mean(rand_times):.6f} sec")
        print("-------------------------------------------")
