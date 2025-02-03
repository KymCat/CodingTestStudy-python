import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n) :
    info = list(map(int, sys.stdin.readline().split()))
    num = info[0]
    queue = deque(info[1:])

    while True :
        node = queue.popleft()
        if node == - 1 : break

        dist = queue.popleft()
        graph[num].append((node, dist)) # 노드 거리

def dfs(start) :
    stack = [(start, 0)]
    visited = set()
    max_tree_len = 0
    max_node = 1

    while stack:
        x, y = stack.pop()
        if x not in visited:
            visited.add(x)
            if max_tree_len < y :
                max_tree_len = y
                max_node = x

            for node, dist in graph[x]:
                if node not in visited:
                    stack.append((node, dist + y))

    return (max_node,max_tree_len)

max_node, max_tree_len = dfs(1)
print(max(max_tree_len, dfs(max_node)[1]))

# 트리는 모든 노드가 연결되어 있는 그래프
# dfs를 두번 하는 이유는, 첫번째로 start한 노드가 트리의 끝점이라는 보장이 없기 때문임 !
# 따라서 아무노드로 처음에 dfs하여 끝에 있는 노드를 찾고 그 이후에 한번 더 dfs하여 지름을 구하는 것 !
# 끝점 노드 < -- 지름 -- > 끝점 노드