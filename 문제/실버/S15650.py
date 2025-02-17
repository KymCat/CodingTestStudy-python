import sys, itertools

n,m = map(int, sys.stdin.readline().split())
arr = [ i for i in range(1,n+1) ]

for i in itertools.combinations(arr,m) :
    print(*i)