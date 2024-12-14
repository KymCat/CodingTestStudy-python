import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
maps = [ list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(maps) :
    queue = deque([(0,0)])

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[x][y] == 0 :
                continue

            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    return maps[n-1][m-1]

print(bfs(maps))

