def dfs(u, t, f, vis, R):
    if u == t: return f
    vis.add(u)
    for v in range(len(R)):
        if v not in vis and R[u][v] > 0:
            pushed = dfs(v, t, min(f, R[u][v]), vis, R)
            if pushed: R[u][v] -= pushed; R[v][u] += pushed; return pushed
    return 0

def maxflow(R, s, t):
    flow = 0
    while True:
        p = dfs(s, t, 1e9, set(), R)
        if not p: break
        flow += p
    return flow

R = [[0]*6 for _ in range(6)]
R[4][0]=R[4][1]=1; R[0][2]=R[0][3]=1; R[1][3]=1; R[2][5]=R[3][5]=1  # source=4, sink=5

print("Maximum Matching =", maxflow(R, 4, 5))
