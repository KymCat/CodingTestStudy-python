import sys
from itertools import combinations

n,m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

cm = list(combinations(arr,3))
result  = [ sum(i) for i in cm if sum(i) <= m]
print(max(result))

