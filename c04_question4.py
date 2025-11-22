def ori(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def intersect(p1,q1,p2,q2):
    o1,o2=ori(p1,q1,p2),ori(p1,q1,q2)
    o3,o4=ori(p2,q2,p1),ori(p2,q2,q1)
    return o1*o2<0 and o3*o4<0

segs=[((1,1),(4,4)), ((1,4),(4,1)), ((2,5),(6,5)), ((3,3),(7,3))]

found=False
for i in range(len(segs)):
    for j in range(i+1,len(segs)):
        if intersect(*segs[i],*segs[j]):
            print("Intersection:", segs[i], segs[j]); found=True

if not found: print("No intersections found")
