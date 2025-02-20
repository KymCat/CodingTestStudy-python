import sys, itertools

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in list(itertools.permutations(arr,m)) :
    print(*i)