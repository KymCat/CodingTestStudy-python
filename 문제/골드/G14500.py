import sys

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, sys.stdin.readline().split())))

max_value = max(map(max, graph))
visited = [[0] * m for _ in range(n)]


def dfs(idx, x, y, visited, total) :
    global answer # 솔직히 전역변수 쓰는거 마음에 안듬...

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    if idx == 4 :
        answer = max(answer, total)
        return

    elif answer >= total + (max_value * (4-idx)) :
        return

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
            visited[nx][ny] = 1
            if idx == 2 :
                dfs(idx+1, x, y, visited, total + graph[nx][ny])
            dfs(idx + 1, nx, ny, visited, total + graph[nx][ny])
            visited[nx][ny] = 0


answer = -1
for i in range(n) :
    for j in range(m) :
        visited[i][j] = 1
        dfs(1, i, j, visited, graph[i][j])
        visited[i][j] = 0

print(answer)