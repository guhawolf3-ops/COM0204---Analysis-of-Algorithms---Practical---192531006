import time
import random

# ---------------------------
# 1️⃣ Linear Search  (O(n))
# ---------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------------------------
# 2️⃣ Binary Search (O(log n))
# ---------------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ----------------------------------------------
# 3️⃣ Sum of first n natural numbers (Iterative)
# ----------------------------------------------
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ----------------------------------------------
# 4️⃣ Sum of first n natural numbers (Recursive)
# ----------------------------------------------
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)


# ---------------------------
# Helper: Measure execution time
# ---------------------------
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


# ---------------------------
# Main Program
# ---------------------------
if __name__ == "__main__":
    input_sizes = [1000, 5000, 10000, 20000, 40000]

    print("---- Time Complexity Analysis ----\n")

    for n in input_sizes:
        arr = list(range(n))
        target = random.choice(arr)

        # Linear Search
        t1 = measure_time(linear_search, arr, target)

        # Binary Search (requires sorted array)
        t2 = measure_time(binary_search, arr, target)

        # Sum iterative
        t3 = measure_time(sum_iterative, n)

        # Sum recursive (limit to small n to avoid recursion depth error)
        if n <= 1000:
            t4 = measure_time(sum_recursive, n)
        else:
            t4 = "Too large for recursion"

        print(f"Input Size: {n}")
        print(f"  Linear Search Time     : {t1:.6f} sec")
        print(f"  Binary Search Time     : {t2:.6f} sec")
        print(f"  Sum (Iterative) Time   : {t3:.6f} sec")
        print(f"  Sum (Recursive) Time   : {t4}")
        print("--------------------------------------")
