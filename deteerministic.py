import random
import time
import statistics

# --------------------------------------
# 1️⃣ Deterministic QuickSelect (fixed pivot = last element)
# --------------------------------------
def deterministic_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(left):
        return deterministic_select(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return deterministic_select(right, k - len(left) - len(equal))


# --------------------------------------
# 2️⃣ Randomized QuickSelect (random pivot)
# --------------------------------------
def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(left):
        return randomized_select(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return randomized_select(right, k - len(left) - len(equal))


# --------------------------------------
# 3️⃣ Helper: measure execution time
# --------------------------------------
def measure_time(func, arr, k):
    start = time.time()
    func(arr, k)
    return time.time() - start


# --------------------------------------
# 4️⃣ Main Program
# --------------------------------------
if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]
    trials = 5

    print("---- Randomized vs Deterministic Selection ----\n")

    for n in sizes:
        det_times = []
        rand_times = []

        for _ in range(trials):
            arr = [random.randint(1, 10000) for _ in range(n)]
            k = random.randint(1, n)

            det_times.append(measure_time(deterministic_select, arr, k))
            rand_times.append(measure_time(randomized_select, arr, k))

        print(f"Array Size: {n}, Random k = {k}")
        print(f"  Deterministic Select Avg Time: {statistics.mean(det_times):.6f} sec")
        print(f"  Randomized Select Avg Time   : {statistics.mean(rand_times):.6f} sec")
        print("-------------------------------------------")
