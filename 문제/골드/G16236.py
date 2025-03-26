import sys
from collections import deque

n = int(sys.stdin.readline())

INF = int(1e9)
shark_x, shark_y = 0,0
maps = []
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    if 9 in row :
        shark_x, shark_y = i, row.index(9)
    maps.append(row)

shark_size = 2
shark_size_stack = 0
def fish_search(cur_x, cur_y) : # 현재 아기상어 위치
    result = (INF, n, n) # time, x, y

    visited = set()
    visited.add((cur_x, cur_y))
    q = deque([(cur_x, cur_y, 0)])
    while q :
        x,y,time = q.popleft()
        if 0 < maps[x][y] < shark_size and maps[x][y] != 9 : # 먹을 수 있는 먹이면,
            result = min(result, (time, x, y)) # 거리(시간)이 같을 때 위, 왼쪽 먹이가 우선권 !
        elif result[0] < time : continue

        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)] :
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] <= shark_size:
                if (nx,ny) not in visited :
                    q.append((nx,ny,time+1))
                    visited.add((nx,ny))

    return result
def solution(cur_x, cur_y) :
    global shark_size, shark_size_stack
    time = 0

    while True :
        result, nx, ny = fish_search(cur_x, cur_y) # 시간, 이동좌표 반환
        if result == INF : return time

        maps[cur_x][cur_y], maps[nx][ny] = 0,9
        cur_x,cur_y = nx,ny

        time += result
        shark_size_stack += 1
        if shark_size_stack == shark_size :
            shark_size_stack = 0
            shark_size+=1

print(solution(shark_x,shark_y))