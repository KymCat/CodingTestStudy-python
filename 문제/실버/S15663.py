import sys, itertools

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = list(set(itertools.permutations(arr,m)))
ans.sort()
for i in ans :
    print(*i)