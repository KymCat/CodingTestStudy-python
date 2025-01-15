import sys
from collections import deque

n,m = map(int, input().split())

maps = []
for _ in range(n) :
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0] # L R U D
dy = [0, 0, -1, 1] # L R U D

def bfs() :
    queue = deque([(0,0)]) # 문제에선 1,1 인데 인덱스로 바꾸면 0,0임

    visited = set()
    visited.add((0,0))

    cnt = 0
    while queue :
        x,y = queue.popleft()
        if x == n-1 and y == m-1 : # 목적지 도착
            return maps[x][y]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 0 :
                continue

            if (nx,ny) not in visited :
                maps[nx][ny] += maps[x][y]
                queue.append((nx,ny))
                visited.add((nx,ny))

print(bfs())