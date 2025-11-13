import random
import time

# ---------------------------------
# 1️⃣ Monte Carlo Algorithm — Fermat’s Primality Test
# ---------------------------------
def is_probably_prime(n, k=5):
    """Monte Carlo algorithm — may be wrong with small probability"""
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False  # Definitely composite
    return True  # Probably prime


# ---------------------------------
# 2️⃣ Las Vegas Algorithm — Randomized QuickSort
# ---------------------------------
def randomized_quicksort(arr):
    """Las Vegas algorithm — always correct, random runtime"""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + mid + randomized_quicksort(right)


# ---------------------------------
# 3️⃣ Helper functions for timing
# ---------------------------------
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


# ---------------------------------
# 4️⃣ Main Program
# ---------------------------------
if __name__ == "__main__":
    print("---- Monte Carlo vs Las Vegas Algorithms ----\n")

    # Monte Carlo: Fermat’s Primality Test
    n = 1013  # a prime number
    result, t1 = measure_time(is_probably_prime, n, 5)
    print(f"Monte Carlo (Fermat Test) for n = {n}")
    print(f"  Result: {'Probably Prime' if result else 'Composite'}")
    print(f"  Execution Time: {t1:.6f} sec\n")

    # Las Vegas: Randomized QuickSort
    arr = [random.randint(1, 10000) for _ in range(1000)]
    _, t2 = measure_time(randomized_quicksort, arr)
    print("Las Vegas (Randomized QuickSort) on 1000 elements")
    print("  Result: Correctly Sorted =", arr == sorted(arr))
    print(f"  Execution Time: {t2:.6f} sec\n")

    print("Monte Carlo → May be wrong but fast (probabilistic correctness).")
    print("Las Vegas  → Always correct but time varies (probabilistic runtime).")
