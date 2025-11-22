def push_relabel(C, s, t):
    n=len(C); F=[[0]*n for _ in range(n)]
    h=[0]*n; h[s]=n
    excess=[0]*n
    for v in range(n): F[s][v]=C[s][v]; excess[v]=C[s][v]
    def push(u,v): f=min(excess[u], C[u][v]-F[u][v]); F[u][v]+=f; F[v][u]-=f; excess[u]-=f; excess[v]+=f
    def relabel(u): h[u]=1+min(h[v] for v in range(n) if C[u][v]-F[u][v]>0)
    changed=True
    while changed:
        changed=False
        for u in range(n):
            if u not in (s,t) and excess[u]>0:
                for v in range(n):
                    if C[u][v]-F[u][v]>0 and h[u]==h[v]+1: push(u,v); changed=True; break
                else: relabel(u); changed=True
    return sum(F[s][i] for i in range(n))

C = [[0,10,5,0],[0,0,15,10],[0,0,0,10],[0,0,0,0]]
print("Max Flow =", push_relabel(C, 0, 3))
