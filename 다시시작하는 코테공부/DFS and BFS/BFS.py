from collections import deque

def bfs_deque(graph,v,visited) :
    queue = deque([v])
    visited[v] = True

    while queue :
        value = queue.popleft()
        print(value, end=" ")

        for i in graph[value] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs_deque(graph,1,visited)