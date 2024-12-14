import sys

n,m = map(int,sys.stdin.readline().split())
maps = [ list(map(int,sys.stdin.readline().strip())) for _ in range(n) ]

def dfs(x,y) :
    if maps[x][y] == 1 :
        return False

    stack = [(x,y)]
    while stack :
        nx,ny = stack.pop()

        if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 1 :
            continue

        maps[nx][ny] = 1
        stack.append((nx+1,ny))
        stack.append((nx-1,ny))
        stack.append((nx,ny-1))
        stack.append((nx,ny+1))

    return True

count = 0
for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 0 and dfs(i,j) :
            count+=1

print(count)