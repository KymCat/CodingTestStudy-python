# BFS Soultion / faster than Floyd-Warshall

import sys
from collections import deque

INF = int(1e9)
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start) :
    queue = deque([start])
    visited = set()
    visited.add(start)
    kevin = [0] * (n+1)

    while queue :
        node = queue.popleft()

        for i in graph[node] :
            if i not in visited :
                kevin[i] = kevin[node] + 1
                visited.add(i)
                queue.append(i)

    return sum(kevin)

sum_list = [INF] # 첫번째항은 INF / 인덱스와 사람번호를 맞추기위해
for i in range(1,n+1) :
    sum_list.append(bfs(i))

print(sum_list.index(min(sum_list)))
