import itertools, time

W = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]  # 4-city cost matrix

def brute_tsp(W):
    n, best = len(W), float('inf')
    for p in itertools.permutations(range(1,n)):
        d = W[0][p[0]] + sum(W[p[i]][p[i+1]] for i in range(n-2)) + W[p[-1]][0]
        best = min(best, d)
    return best

def dp_tsp(W):
    n = len(W); dp = {(1<<0,0):0}
    for mask in range(1<<n):
        for u in range(n):
            if (mask,u) in dp:
                for v in range(n):
                    if not mask&(1<<v):
                        dp[(mask|(1<<v),v)] = min(dp.get((mask|(1<<v),v),1e9), dp[(mask,u)] + W[u][v])
    full = (1<<n)-1
    return min(dp[(full,u)] + W[u][0] for u in range(1,n))

t1=time.time(); b=brute_tsp(W); t1=time.time()-t1
t2=time.time(); d=dp_tsp(W); t2=time.time()-t2

print("Brute-force:", b, "Time:", round(t1,6))
print("DP (Held-Karp):", d, "Time:", round(t2,6))
