import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n) :
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[ [0] * 2 for _ in range(m)] for _ in range(n)]

def bfs() :
    queue = deque()
    queue.append((0,0,0)) # x,y,is_wall_break

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue :
        x,y,wall = queue.popleft()
        if x == n-1 and y == m-1 :
            return visited[x][y][wall] + 1

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0 :
                if maps[nx][ny] == 0 :
                    queue.append((nx,ny,wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

                elif maps[nx][ny] == 1 and not wall :
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][wall] + 1
    return -1

print(bfs())

