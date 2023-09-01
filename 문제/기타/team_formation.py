import sys

input = sys.stdin.readline
n,m = map(int, input().split())

parent = [0] * (n+1)
for i in range(0, n+1) :
    parent[i] = i
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

edges = []
for _ in range(m) :
    cal, a, b = map(int, input().split())
    edges.append((cal,a,b))

for edge in edges :
    cal, a, b = edge
    if cal == 1 :
        if find_parent(parent,a) == find_parent(parent,b) :
            print('YES')
        else :
            print('NO')
    else :
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent,a,b)


