import sys
n = int(input())
maps = []
for _ in range(n) :
    maps.append(list(map(int,sys.stdin.readline().rstrip())))

def dfs(maps, visited, group, i,j) :
    stack = [(i,j)]
    group.append(0)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while stack :
        x,y = stack.pop()
        if (x,y) not in visited :
            group[len(group) -1] += 1
            visited.add((x,y))

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n or maps[nx][ny] == 0 or (nx,ny) in visited :
                    continue

                stack.append((nx,ny))

group = []
visited = set()
for i in range(n) :
    for j in range(n) :
        if maps[i][j] == 1 and (i,j) not in visited  :
            dfs(maps,visited,group,i,j)

print(len(group))
for i in sorted(group) :
    print(i)
