class Node:
    def __init__(self, k, c="R"): self.k, self.c, self.l, self.r = k, c, None, None

def rotate_left(x):
    y = x.r; x.r = y.l; y.l = x; return y

def rotate_right(x):
    y = x.l; x.l = y.r; y.r = x; return y

def insert(root, k):
    if not root: return Node(k, "B")
    if k < root.k: root.l = insert(root.l, k)
    else: root.r = insert(root.r, k)

    if root.r and root.r.c == "R" and not (root.l and root.l.c == "R"):
        root = rotate_left(root)
    if root.l and root.l.c == "R" and root.l.l and root.l.l.c == "R":
        root = rotate_right(root)
    if root.l and root.l.c == "R" and root.r and root.r.c == "R":
        root.c = "R"; root.l.c = root.r.c = "B"
    return root
