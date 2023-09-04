n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

p = []
for i in a :
    p.append(b.index(i))
    b[b.index(i)] = -1

print(*p)