import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0
for _ in range(n) :
    min_a = a.pop(a.index(min(a)))
    max_b = b.pop(b.index(max(b)))
    result = result + (min_a * max_b)

print(result)





