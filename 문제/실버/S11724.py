import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(visited,start) :
    stack = [start]

    while stack :
        node = stack.pop()
        if node not in visited :
            visited.add(node)

            for i in graph[node] :
                if i not in visited :
                    stack.append(i)

visited = set()
cnt = 0
for i in range(1,n+1) :
    if i not in visited :
        dfs(visited,i)
        cnt+=1

print(cnt)