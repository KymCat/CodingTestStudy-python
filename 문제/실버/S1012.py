import sys
t = int(sys.stdin.readline())
def dfs(maps,x,y) :
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    stack = [(x,y)]
    while stack :
        row,col = stack.pop()
        if maps[row][col] :
            maps[row][col] = 0

        for i in range(4) :
            nx = row + dx[i]
            ny = col + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0 or maps[nx][ny] == 0:
                continue

            stack.append((nx,ny))


for _ in range(t) :
    n,m,k = map(int, sys.stdin.readline().split())
    maps = [ [0] * m for i in range(n)]
    cabbage = []
    for _ in range(k) :
        x,y = map(int, sys.stdin.readline().split())
        maps[x][y] = 1
        cabbage.append((x,y))

    cnt = 0
    for x,y in cabbage :
        if maps[x][y] == 0 :
            continue
        dfs(maps,x,y)
        cnt += 1

    print(cnt)

