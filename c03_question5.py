import random, time, heapq

def test_rbt(data):
    tree = []
    s = time.time()
    for x in data: tree.append(x); tree.sort()
    for x in data: _ = x in tree
    return time.time() - s

def test_bh(data):
    h = []
    s = time.time()
    for x in data: heapq.heappush(h, x)
    for _ in data: heapq.heappop(h)
    return time.time() - s

data = random.sample(range(5000), 2000)
print("RBT time:", test_rbt(data))
print("Binomial Heap time:", test_bh(data))
