import sys
from collections import deque

n = int(input())

graph = [[] for _ in range(n)] # 인접리스트
for i in range(n) :
    row = map(int, sys.stdin.readline().split())
    for index, value in enumerate(row) :
        if value == 1 : graph[i].append(index)

adj_mx = [[0] * n for _ in range(n)]
for i in range(n) :
    queue = deque()
    queue.append(i)

    visited = set()

    while queue :
        node = queue.popleft()

        for x in graph[node] :
            if x not in visited :
                adj_mx[i][x] = 1
                queue.append(x)
                visited.add(x)


for row in adj_mx :
    print(*row)