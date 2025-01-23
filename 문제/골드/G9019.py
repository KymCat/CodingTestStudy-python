import sys
from collections import deque
# pypy3
def bfs(A,B) :
    queue = deque()
    queue.append((A, ''))

    visited = [False] * 10000
    visited[A] = True

    while queue :
        x, path = queue.popleft()
        if x == B :
            return path

        D = (2*x) % 10000
        if not visited[D] :
            visited[D] = True
            queue.append((D,path + 'D'))

        S = (x-1) % 10000
        if not visited[S] :
            visited[S] = True
            queue.append((S,path + 'S'))

        L = (x%1000) * 10 + (x//1000)
        if not visited[L] :
            visited[L] = True
            queue.append((L,path + 'L'))

        R = (x%10) * 1000 + (x//10)
        if not visited[R] :
            visited[R] = True
            queue.append((R,path + 'R'))

t = int(input())

for _ in range(t) :
    A,B = map(int, sys.stdin.readline().split())
    print(bfs(A,B))
