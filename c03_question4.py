class Node:
    def __init__(self, k): self.k, self.c, self.ch = k, 0, []

def link(a, b):
    if a.k > b.k: a, b = b, a
    b.c += 1; a.ch.append(b); return a

def merge(h1, h2):
    h = sorted(h1 + h2, key=lambda x: x.c)
    i = 0
    while i < len(h)-1 and h[i].c == h[i+1].c:
        h[i] = link(h[i], h.pop(i+1))
    return h

def extract_min(h):
    m = min(h, key=lambda x: x.k); h.remove(m)
    return merge(h, m.ch), m.k

def decrease_key(node, new_k):
    node.k = new_k
    for c in node.ch:
        if c.k < node.k: node.k, c.k = c.k, node.k
