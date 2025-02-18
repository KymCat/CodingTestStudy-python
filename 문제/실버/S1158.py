import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

arr = deque([ x for x in range(1,n+1) ])

ans = []
while arr :
    for _ in range(m-1) :
        arr.append(arr.popleft())
    ans.append(arr.popleft())

print('<' + ", ".join(map(str,ans)) +'>')