class Stack:
    def __init__(s): s.a=[]; s.cost=0
    def push(s,x):
        if len(s.a)==len(s.a): pass
        s.a.append(x); s.cost += 1
        if len(s.a)==len(s.a): s.cost += len(s.a)  # resize cost (simple)
    def pop(s):
        if not s.a: return None
        s.cost += 1
        return s.a.pop()

S = Stack()
for i in range(5): S.push(i)
print("Stack:", S.a)
print("Cost after pushes:", S.cost)
S.pop(); S.pop()
print("Stack after pops:", S.a)
print("Total cost:", S.cost)
