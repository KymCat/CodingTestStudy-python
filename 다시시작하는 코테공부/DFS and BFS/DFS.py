def dfs_stack(graph, v, visited) : #그래프, 시작노드, 방문노드
    stack = [v]

    while stack :
        value = stack.pop()
        if not visited[value] :
            visited[value] = True
            print(value, end=" ")

            for i in reversed(graph[value]) :
                if not visited[i] :
                    stack.append(i)


def dfs_stack_visited_set(graph, v) : # visiteed 함수를 set으로 만든 dfs
    stack = [v]
    visited = set()

    while stack :
        value = stack.pop()
        if value not in visited :
            visited.add(value)
            print(value, end=" ")

            for i in reversed(graph[value]) :
                if i not in visited :
                    stack.append(i)


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
dfs_stack(graph,1,visited)
print("")
dfs_stack_visited_set(graph,1)