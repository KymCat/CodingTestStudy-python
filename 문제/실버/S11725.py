import sys
from collections import deque

n = int(input())

parent = [0] * (n+1)
parent[1] = 1

graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start) :
    queue = deque([start])

    while queue :
        x = queue.popleft()

        for i in graph[x] :
            if parent[i] == 0 :
                parent[i] = x
                queue.append(i)

bfs(1)
for i in range(2,n+1) :
    print(parent[i])