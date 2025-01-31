import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

start = (0,0)
campus = []
for i in range(n) :
    row = list(map(str, sys.stdin.readline().rstrip()))
    if 'I' in row :
        start = (i, row.index('I'))

    campus.append(row)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = set()
visited.add(start)

answer = 0
queue = deque()
queue.append(start)
while queue :
    x,y = queue.popleft()

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and campus[nx][ny] != 'X' :
            if campus[nx][ny] == 'P' :
                answer+=1

            queue.append((nx,ny))
            visited.add((nx,ny))

if answer :
    print(answer)
else : print('TT')
