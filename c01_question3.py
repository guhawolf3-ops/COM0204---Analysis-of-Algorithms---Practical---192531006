def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)

def binary_search(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x: return m
        elif a[m] < x: l = m+1
        else: r = m-1
    return -1

print("Factorial(5):", fact(5))     # For induction proof
arr_unsorted = [7, 2, 9, 1, 6]
print("Binary Search on unsorted:", binary_search(arr_unsorted, 1))
print("Sorted Array Search:", binary_search(sorted(arr_unsorted), 1))
