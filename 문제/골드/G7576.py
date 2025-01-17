import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

tomato = []
for _ in range(m) :
    tomato.append(list(map(int,sys.stdin.readline().split())))

ripe = deque()
visited = set()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(m) :
    for j in range(n) :
        if tomato[i][j] == 1 :
            ripe.append((i,j))

cnt = 0
while ripe :
    x,y = ripe.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n \
                or (nx, ny) in visited or tomato[nx][ny] == -1 or tomato[nx][ny] >= 1:
            continue

        tomato[nx][ny] = tomato[x][y] + 1
        visited.add((nx, ny))
        ripe.append((nx, ny))
    cnt = tomato[x][y]


for i in range(m) :
    if 0 in tomato[i] :
        cnt = 0
        break

print(cnt-1)