import sys, copy
from collections import deque
from itertools import combinations

def bfs(maps) :
    q = deque(virus)
    safe_count = safe
    global ans

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 :
                maps[nx][ny] = 2
                safe_count-=1
                if safe_count <= ans : return safe_count
                q.append((nx, ny))
    return safe_count

n,m = map(int, sys.stdin.readline().split())

safe = 0
maps = []
virus = []
wall = []
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    maps.append(row)

    for j in range(m) :
        if row[j] == 2 :
            virus.append((i,j))
        elif row[j] == 0 :
            safe+=1
            wall.append((i,j))

ans = 0
for cb in combinations(wall, 3) :
    cpy_maps = copy.deepcopy(maps)
    for x,y in cb :
        cpy_maps[x][y] = 1
    ans = max(ans, bfs(cpy_maps))

print(ans-3)
