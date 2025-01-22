import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())

tomato = []
for i in range(h) : # 3차원 리스트
    layer = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    tomato.append(layer)

visited = [[[0] * m for _ in range(n)] for _ in range(h)]

queue = deque()
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if tomato[i][j][k] == 1 :
                queue.append((i,j,k))
                visited[i][j][k] = 1


dh = [0,0,0,0,-1,1] # L R U D F B
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]

day = 0
while queue :
    z,x,y = queue.popleft()

    for s in range(6) :
        nz = z + dh[s]
        nx = x + dx[s]
        ny = y + dy[s]

        if nz < 0 or nx < 0 or ny < 0 or nz >= h or nx >= n or ny >= m or visited[nz][nx][ny] == 1 or tomato[nz][nx][ny] == - 1 or tomato[nz][nx][ny] >= 1:
            continue

        queue.append((nz,nx,ny))
        tomato[nz][nx][ny] += tomato[z][x][y] + 1
        visited[nz][nx][ny] = 1
    day = tomato[z][x][y]


flag = True
for i in range(h) :
    for j in range(n) :
        if 0 in tomato[i][j] :
            flag = False
            break
    if not flag : break

if flag :
    print(day-1)
else : print(-1)
