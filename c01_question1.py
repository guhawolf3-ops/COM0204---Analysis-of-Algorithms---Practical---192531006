import time, random

def linear_search(a, x): 
    for i in range(len(a)): 
        if a[i] == x: return i
    return -1

def binary_search(a, x):
    l, r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x: return m
        elif a[m] < x: l = m+1
        else: r = m-1
    return -1

for n in [1000, 5000, 10000]:
    arr = list(range(n)); x = random.choice(arr)
    print("\nSize:", n)
    t = time.time(); linear_search(arr, x); print("Linear:", round(time.time()-t,6))
    t = time.time(); binary_search(arr, x); print("Binary:", round(time.time()-t,6))
