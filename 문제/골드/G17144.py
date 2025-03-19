import sys

r,c,t = map(int, sys.stdin.readline().split())

maps = []
for i in range(r) :
    maps.append(list(map(int, sys.stdin.readline().split())))

air = 0
for i in range(r) :
    if maps[i][0] == -1 :
        air= i
        break
def air_circulation(x) :
    # top-side
    for i in range(x-1,0,-1) :
        maps[i][0] = maps[i-1][0]

    for i in range(c-1) :
        maps[0][i] = maps[0][i+1]

    for i in range(x) :
        maps[i][c-1] = maps[i+1][c-1]

    for i in range(c-1,1,-1) :
        maps[x][i] = maps[x][i-1]
    maps[x][1] = 0

    # down-side
    for k in range(x+2,r-1) :
        maps[k][0] = maps[k+1][0]

    for k in range(c-1) :
        maps[r-1][k] = maps[r-1][k+1]

    for k in range(r-1, x, -1) :
        maps[k][c-1] = maps[k-1][c-1]

    for k in range(c-1,1,-1) :
        maps[x+1][k] = maps[x+1][k-1]
    maps[x+1][1] = 0

def dust_spread() :
    global maps

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dust = []
    for x in range(r) :
        for y in range(c) :
            if maps[x][y] == - 1 : continue
            elif maps[x][y] :
                dust.append([x,y,maps[x][y]])

    for x,y,value in dust :
        cnt = 0
        spread = [0, 0, 0, 0]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != -1 :
                spread[i] = 1
                cnt+=1
        LArc = value//5
        maps[x][y] -= (LArc * cnt)
        for i in range(4) :
            if spread[i] :
                maps[x+dx[i]][y+dy[i]] += LArc

    air_circulation(air)

for i in range(t) :
    dust_spread()

print(sum(sum(i) for i in maps) + 2)
