class Node:
    def __init__(self, k): self.k, self.c, self.ch = k, 0, []

def link(b1, b2):
    if b1.k > b2.k: b1, b2 = b2, b1
    b2.c += 1; b1.ch.append(b2); return b1

def merge(h1, h2):
    h = h1 + h2; h.sort(key=lambda x: x.c)
    i = 0
    while i < len(h)-1 and h[i].c == h[i+1].c:
        h[i] = link(h[i], h.pop(i+1))
    return h

def insert(h, k): return merge(h, [Node(k)])

def display(h):
    for t in h: print(f"B{t.c} root={t.k} children={[c.k for c in t.ch]}")
