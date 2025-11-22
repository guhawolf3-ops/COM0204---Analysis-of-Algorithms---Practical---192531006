import itertools, time

graph = {1:[2,3], 2:[1,3], 3:[1,2]}

def brute_force_vc(g):
    edges = {(u,v) for u in g for v in g[u] if u<v}
    V = list(g.keys())
    for r in range(len(V)+1):
        for subset in itertools.combinations(V, r):
            if all(u in subset or v in subset for (u,v) in edges):
                return subset

def approx_vc(g):
    E = {(u,v) for u in g for v in g[u] if u<v}
    C = set()
    while E:
        u,v = E.pop()
        C.update([u,v])
        E = {(x,y) for (x,y) in E if x not in C and y not in C}
    return C

start = time.time(); bf = brute_force_vc(graph); t1 = time.time()-start
start = time.time(); ap = approx_vc(graph); t2 = time.time()-start

print("Brute-force VC:", bf, "Time:", round(t1,6))
print("Approx VC:", ap, "Time:", round(t2,6))
