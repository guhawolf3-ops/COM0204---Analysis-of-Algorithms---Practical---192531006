class DynamicTable:
    def __init__(s): s.a=[]; s.cap=1; s.moves=0
    def insert(s,x):
        if len(s.a)==s.cap:
            s.cap*=2; s.moves+=len(s.a)     # movements during doubling
        s.a.append(x)
    def delete(s):
        if not s.a: return
        s.a.pop()
        if len(s.a) < s.cap//2:
            s.cap//=2; s.moves+=len(s.a)   # movements during shrinking

T = DynamicTable()
for i in range(5): T.insert(i)
T.delete(); T.delete()
print("Array:", T.a)
print("Capacity:", T.cap)
print("Total movements:", T.moves)
