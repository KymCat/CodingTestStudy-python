import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())
graph = []
for _ in range(m) :
    graph.append(list(map(int, sys.stdin.readline().split())))

# 인접리스트 형태로 만들기
adj_list = [[] for _ in range(n+1)] # 0정점까지 해서 +1
for i,j in graph :
        adj_list[i].append(j)
        adj_list[j].append(i)

for i in range(1,n+1) : # 각 행마다 오름차순으로 정리
    adj_list[i].sort()

def dfs(adj_list, start) :
    stack = [start]
    visited = set()

    while stack :
        value = stack.pop()
        if value not in visited :
            print(value, end=" ")
            visited.add(value)

            for i in reversed(adj_list[value]) :
                if i not in visited :
                    stack.append(i)

def bfs(adj_list, start) :
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue :
        value = queue.popleft()
        print(value, end=" ")

        for i in adj_list[value] :
            if i not in visited :
                queue.append(i)
                visited.add(i)


dfs(adj_list, v)
print()
bfs(adj_list, v)