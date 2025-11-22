import itertools

clauses = [[("x1",True),("x2",False),("x3",True)],
           [("x1",False),("x2",True),("x3",True)],
           [("x1",True),("x2",True),("x3",False)]]

V = [(i,l) for i,c in enumerate(clauses) for l in c]
E = {(a,b) for a,b in itertools.combinations(V,2)
     if a[0] != b[0] and not (a[1][0]==b[1][0] and a[1][1]!=b[1][1])}

def is_k_clique(k):
    for comb in itertools.combinations(V,k):
        if all((u,v) in E or (v,u) in E for u,v in itertools.combinations(comb,2)):
            return True
    return False

k = len(clauses)
print("3-SAT Satisfiable via Clique:", is_k_clique(k))
