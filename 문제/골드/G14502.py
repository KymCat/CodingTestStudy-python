import sys, copy
from collections import deque

n,m = map(int, sys.stdin.readline().split())

maps = []
virus = []
safe = 0
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    maps.append(row)

    for j in range(m) :
        if row[j] == 2 :
            virus.append((i,j))
        elif row[j] == 0 :
            safe+=1

ans = 0
def bfs() :
    q = deque(virus)
    cpy_maps = copy.deepcopy(maps)
    safe_count = safe
    global ans

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and cpy_maps[nx][ny] == 0 :
                cpy_maps[nx][ny] = 2
                safe_count-=1
                if safe_count <= ans : return
                q.append((nx, ny))
    ans = max(ans, safe_count)

def wall(cnt) :
    if cnt == 3 :
        bfs()
        return

    else :
        for i in range(n) :
            for j in range(m) :
                if maps[i][j] == 0 :
                    maps[i][j] = 1
                    wall(cnt+1)
                    maps[i][j] = 0

wall(0)
print(ans-3) # wall()에서 벽 3개 설치한거 빼기