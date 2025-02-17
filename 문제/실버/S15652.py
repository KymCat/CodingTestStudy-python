import sys, itertools

n,m = map(int, sys.stdin.readline().split())
arr = [ x for x in range(1,n+1) ]

for i in itertools.combinations_with_replacement(arr,m) :
    print(*i)