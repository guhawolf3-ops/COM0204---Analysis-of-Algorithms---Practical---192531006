def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a)//2
    return merge(merge_sort(a[:m]), merge_sort(a[m:]))

def merge(l, r):
    res = []
    while l and r:
        res.append((l if l[0] < r[0] else r).pop(0))
    return res + l + r

def quick_sort(a):
    if len(a) <= 1: return a
    p = a[0]
    return quick_sort([x for x in a[1:] if x < p]) + [p] + quick_sort([x for x in a[1:] if x >= p])

class BST:
    def __init__(s,v): s.v=v; s.l=s.r=None
    def insert(s,x):
        if x < s.v: s.l = BST(x) if not s.l else s.l.insert(x)
        else: s.r = BST(x) if not s.r else s.r.insert(x)

arr = [5,3,8,1,4]
print("Merge:", merge_sort(arr))
print("Quick:", quick_sort(arr))
t = BST(5); [t.insert(x) for x in [3,8,1,4]]
print("BST Root:", t.v)
