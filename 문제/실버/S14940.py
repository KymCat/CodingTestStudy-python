import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
visited = [[0] * m for _ in range(n)]

maps = []
start = ((0,0))
for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    if 2 in tmp :
        start = (i,tmp.index(2))
    maps.append(tmp)

maps[start[0]][start[1]] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(maps, visited, start) :
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m \
                    or visited[nx][ny] == 1  or maps[nx][ny] == 0:
                continue
            queue.append((nx,ny))
            maps[nx][ny] += maps[x][y]
            visited[nx][ny] = 1


    for i in range(n) :
        for j in range(m) :
            if visited[i][j] == 0 and maps[i][j] == 1:
                maps[i][j] = -1


bfs(maps, visited, start)
for i in maps :
    print(*i)


