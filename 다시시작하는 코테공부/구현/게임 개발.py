import sys

n,m = map(int, sys.stdin.readline().split()) # 맵크기 n x m
x,y,direction = map(int, sys.stdin.readline().split()) # 초기좌표와 보고있는 방향(0:북쪽 1:동쪽 2:남쪽 3:서쪽)

maps = [] # 맵에서 0은 육지, 1은 바다
for _ in range(n) : # 맵 입력
    maps.append(list(map(int, sys.stdin.readline().split())))

visited = [[0] * m for _ in range(n)] # 방문좌표
visited[x][y] = 1

def turn_left() :
    global direction
    direction-=1
    if direction < 0 :
        direction = 3

# 이동: 북(-1,0) 동(0,-1) 남(+1,0) 서(0, +1)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

count = 1
turn_time = 0
while True :
    turn_left() # 왼쪽으로 돌고
    nx = x+dx[direction] # 바로보고 있는 곳의 좌표 미리 설정
    ny = y+dy[direction]

    if visited[nx][ny] == 0 and maps[nx][ny] == 0 : # 방문하지않거나, 육지라면
        x = nx
        y = ny
        visited[x][y] = 1
        turn_time = 0
        count+=1
        continue

    else : # 방문했거나, 바다라면
        turn_time += 1

    if turn_time == 4 : # 사방이 막혀있다면
        nx = x - dx[direction] # 뒤로 BACK
        ny = y - dy[direction]
        if maps[nx][ny] == 0 : # 뒤로 간곳이 육지라면
            x,y = nx,ny # 원래 좌표로 수정
        else : # 뒤로 간곳이 바다라면 무한반복문 종료
            break
        turn_time = 0


print(count)

