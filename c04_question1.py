def dfs(u, t, f, vis, R):
    if u == t: return f
    vis.add(u)
    for v in range(len(R)):
        if v not in vis and R[u][v] > 0:
            pushed = dfs(v, t, min(f, R[u][v]), vis, R)
            if pushed:
                R[u][v] -= pushed
                R[v][u] += pushed
                return pushed
    return 0

def ford_fulkerson(R, s, t):
    flow = 0
    while True:
        pushed = dfs(s, t, float('inf'), set(), R)
        if not pushed: break
        flow += pushed
        print("Augmented:", pushed, "Residual:", R)
    return flow

R = [[0, 8, 0, 0, 3, 0], [0, 0, 9, 0, 0, 0],
     [0, 0, 0, 7, 0, 2], [0, 0, 0, 0, 0, 5],
     [0, 0, 7, 4, 0, 0], [0, 0, 0, 0, 0, 0]]

print("Max Flow =", ford_fulkerson(R, 0, 5))
