import sys
from collections import defaultdict

n = int(sys.stdin.readline())
house = []
house.append([0] * (n+1))
for _ in range(n) :
    house.append([0] + list(map(int, sys.stdin.readline().split())))

status = defaultdict(list)
status['가로'] = [(1,1,'대각선'), (0,1,'가로')]
status['세로'] = [(1,0,'세로'), (1,1,'대각선')]
status['대각선'] = [(1,1,'대각선'), (0,1,'가로'), (1,0,'세로')]

def bfs() :
    q = []
    q.append((1,2,'가로'))
    cnt = 0

    while q :
        x,y,stat = q.pop()
        if x == y == n :
            cnt+=1
            continue

        for dx,dy,nstat in status[stat] :
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= n and 1 <= ny <= n and house[nx][ny] != 1 :
                if nstat == '대각선' and (house[nx][y] == 1 or house[x][ny] == 1) :
                    continue

                elif nx == n and ny != n and nstat == '세로' :
                    continue

                elif ny == n and nx != n and nstat == '가로' :
                    continue

                q.append((nx,ny,nstat))
    return cnt

print(bfs())