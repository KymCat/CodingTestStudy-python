import sys, itertools

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

ans = list(set(itertools.combinations_with_replacement(arr,m)))
ans.sort()
for i in ans :
    print(*i)