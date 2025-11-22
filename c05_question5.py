import itertools, time, random
def dijkstra(n):
    W=[[random.randint(1,10) for _ in range(n)] for _ in range(n)]
    dist=[0]+[999]* (n-1); vis=set()
    for _ in range(n):
        u=min((i for i in range(n) if i not in vis), key=lambda x:dist[x])
        vis.add(u)
        for v in range(n): dist[v]=min(dist[v],dist[u]+W[u][v])
    return dist[-1]

def tsp(n):
    W=[[random.randint(1,10) for _ in range(n)] for _ in range(n)]
    best=1e9
    for p in itertools.permutations(range(1,n)):
        d=W[0][p[0]]+sum(W[p[i]][p[i+1]] for i in range(n-2))+W[p[-1]][0]
        best=min(best,d)
    return best

for n in [5,7,9]:
    t1=time.time(); dijkstra(n); t1=time.time()-t1
    t2=time.time(); tsp(7); t2=time.time()-t2  # keep TSP size fixed for speed
    print(f"n={n}  Dijkstra={round(t1,5)}s  TSP={round(t2,5)}s")
