import sys
from collections import defaultdict

n = int(input())

maps = []
blindness_maps = []
for _ in range(n) :
    row = sys.stdin.readline().rstrip()
    maps.append(row)
    if 'G' in row :
        row = row.replace('G','R')
    blindness_maps.append(row)

rgb = defaultdict(int)
blindness_rgb = defaultdict(int)

visited = set()
blindness_visited = set()

def dfs(maps,visited, color, i, j) :
    stack = [(i,j)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while stack :
        x,y = stack.pop()
        if (x,y) not in visited :
            visited.add((x,y))

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx,ny) in visited or maps[nx][ny] != color :
                    continue

                stack.append((nx,ny))
    return 1

for i in range(n) :
    for j in range(n) :
        if (i,j) not in visited :
            rgb[maps[i][j]] += dfs(maps, visited, maps[i][j], i, j)
        if (i,j) not in blindness_visited :
            blindness_rgb[maps[i][j]] += dfs(blindness_maps, blindness_visited, blindness_maps[i][j], i, j)

print(sum(rgb.values()), sum(blindness_rgb.values()))