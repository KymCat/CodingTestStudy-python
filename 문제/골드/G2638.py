import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

maps = []
cheeze = set()
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(m) :
        if row[j] == 1 :
            cheeze.add((i,j))
    maps.append(row)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
hour = 0

def bfs() :
    q = deque()
    q.append((0,0))

    visited = set()
    visited.add((0,0))

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 and (nx,ny) not in visited :
                q.append((nx,ny))
                visited.add((nx,ny))
                continue

    return visited

while cheeze :
    inner = bfs()

    melt = set()
    for x,y in cheeze :
        cnt = 0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n or 0 <= ny < m :
                if maps[nx][ny] == 0 and (nx,ny) in inner :
                    cnt += 1
                if cnt >= 2 :
                    melt.add((x,y))

    cheeze-=melt
    for x,y in melt :
        maps[x][y] = 0
    hour+=1

print(hour)