import random, math

pts=[(random.randint(0,10),random.randint(0,10)) for _ in range(8)]
def ori(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

pts.sort(); lower=[]
for p in pts:
    while len(lower)>1 and ori(lower[-2],lower[-1],p)<=0: lower.pop()
    lower.append(p)
upper=[]
for p in reversed(pts):
    while len(upper)>1 and ori(upper[-2],upper[-1],p)<=0: upper.pop()
    upper.append(p)
hull=lower[:-1]+upper[:-1]

dist=lambda a,b: math.hypot(a[0]-b[0],a[1]-b[1])
pair=min(((dist(pts[i],pts[j]),(pts[i],pts[j])) 
        for i in range(len(pts)) for j in range(i+1,len(pts))), key=lambda x:x[0])

print("Points =", pts)
print("Convex Hull =", hull)
print("Closest Pair =", pair[1], "Distance =", round(pair[0],2))
