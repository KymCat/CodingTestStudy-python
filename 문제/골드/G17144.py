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
# def air_circulation(x) :
#     # top-side
#     for i in range(x-1,0,-1) :
#         maps[i][0] = maps[i-1][0]
#
#     for i in range(c-1) :
#         maps[0][i] = maps[0][i+1]
#
#     for i in range(x) :
#         maps[i][c-1] = maps[i+1][c-1]
#
#     for i in range(c-1,1,-1) :
#         maps[x][i] = maps[x][i-1]
#     maps[x][1] = 0
#
#     # down-side
#     for k in range(x+2,r-1) :
#         maps[k][0] = maps[k+1][0]
#
#     for k in range(c-1) :
#         maps[r-1][k] = maps[r-1][k+1]
#
#     for k in range(r-1, x, -1) :
#         maps[k][c-1] = maps[k-1][c-1]
#
#     for k in range(c-1,1,-1) :
#         maps[x+1][k] = maps[x+1][k-1]
#     maps[x+1][1] = 0

def air_circulation(start_up_side, start_down_side) :
    #     상  우 하  좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y = start_up_side, 1     # 시작좌표
    idx = 1                     # 오른쪽 부터 시작
    prev = 0                    # 이전 값 저장 (처음은 공기청정기에서 나오는 공기 : 0 )
    # top-side 우 -> 상 -> 하 -> 좌
    while True :
        nx, ny = x+dx[idx], y+dy[idx]
        if x == start_up_side and y == 0 : break # 공기청정기로 돌아왔을 때
        if nx == -1 or ny == -1 or ny == c :     # 벽을 만났을 때
            idx = (idx-1)%4                      # 1(우) -> 0(상) -> 3(하) -> 2(좌) 순
            continue

        maps[x][y], prev = prev, maps[x][y] # swap
        x,y = nx, ny

    x, y = start_down_side, 1   # 시작좌표
    idx = 1                     # 오른쪽 부터 시작
    prev = 0                    # 이전 값 저장 (처음은 공기청정기에서 나오는 공기 : 0 )
    # down-side 우 -> 하 -> 좌 -> 상
    while True:
        nx, ny = x + dx[idx], y + dy[idx]
        if x == start_down_side and y == 0: break  # 공기청정기로 돌아왔을 때
        if nx == r or ny == -1 or ny == c:       # 벽을 만났을 때
            idx = (idx + 1) % 4                  # 1(우) -> 2(하) -> 3(좌) -> 0(상) 순
            continue

        maps[x][y], prev = prev, maps[x][y]  # swap
        x, y = nx, ny

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

    air_circulation(air, air+1)

for i in range(t) :
    dust_spread()

print(sum(sum(i) for i in maps) + 2)
