class Node:
    def __init__(self, k, c="B"): self.k, self.c, self.l, self.r = k, c, None, None

def is_red(n): return n and n.c == "R"

def rotate_left(x): y = x.r; x.r = y.l; y.l = x; return y
def rotate_right(x): y = x.l; x.l = y.r; y.r = x; return y

def delete(root, k):
    if not root: return None
    if k < root.k: root.l = delete(root.l, k)
    elif k > root.k: root.r = delete(root.r, k)
    else: return root.l or root.r  # simplified delete

    if is_red(root.r) and not is_red(root.l): root = rotate_left(root)
    if is_red(root.l) and is_red(root.l.l): root = rotate_right(root)
    if is_red(root.l) and is_red(root.r): root.c = "R"; root.l.c = root.r.c = "B"
    return root

def verify(root):
    if not root: return 1
    lh, rh = verify(root.l), verify(root.r)
    return 0 if lh != rh else lh + (root.c == "B")
