import sys

n = int(input())
arr = []
for _ in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    arr.append((a,b))

for x,y in sorted(arr) :
    print(x,y)