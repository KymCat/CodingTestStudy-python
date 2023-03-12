from collections import deque
n,m = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 재규어 좌표 받기
jaguars = []
for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 2 :
            jaguras.append((i,j))

def bfs(walls) :
    visited = [ [False] * m for _ in range(n) ]
    for wall in walls :
        x,y = wall
        visited[x][y] = True

    for jaguar in jaguars :
        queue = deque()
        queue.append(jaguar)

        while queue :
            x,y = queue.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= n or ny >= m or nx < 0 or ny < 0 :
                    continue
                if visited[nx][ny] or maps[nx][ny] == 1 :
                    continue

                visited[nx][ny] = True
                queue.append((nx,ny))
    count = 0
    # 빈칸 카운트
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 0 and not visited[i][j] :
                count+=1
    return count

result = 0
answer = 0
# 울타리 모든 경우설치하기
# 울타리를 3개를 무조건 설치 해야 되므로 좌표가 3개 필요함 (x1, y1) (x2, y2) (x3, y3)
for x1 in range(n) :
    for y1 in range(m) :
        if maps[x1][y1] != 0 :
            continue

        for x2 in range(n) :
            for y2 in range(m) :
                if maps[x2][y2] != 0 or (x1 == x2 and y1 == y2) :
                    continue

                for x3 in range(n) :
                    for y3 in range(m) :
                        if maps[x3][y3] != 0 or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3) :
                            continue

                        result = bfs([(x1, y1), (x2, y2), (x3, y3)])
                        answer = max(result, answer)

print(answer)
