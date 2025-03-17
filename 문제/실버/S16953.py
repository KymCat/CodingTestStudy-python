import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())

def bfs(start) :
    q = deque()
    q.append((start, 1))

    visited = set()
    visited.add(start)

    while q :
        n,cnt = q.popleft()
        if n == b :
            return cnt

        n_2 = n*2
        if n_2 <= b :
            q.append((n_2,cnt+1))

        n_1 = int(str(n) + '1')
        if n_1 <= b :
            q.append((n_1, cnt+1))
    return -1

print(bfs(a))

