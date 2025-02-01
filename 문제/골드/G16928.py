import sys
from collections import deque
from collections import defaultdict

n,m = map(int, sys.stdin.readline().split())

ladder_snake = defaultdict(int)
for _ in range(n) :
    start, end = map(int, sys.stdin.readline().split())
    ladder_snake[start] = end

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    ladder_snake[start] = end


queue = deque()
queue.append(1)
visited = [0 for _ in range(101)]

while queue :
    x = queue.popleft()
    if x == 100 : break

    for dice in range(6,0,-1) :
        nx = x + dice

        if nx <= 100 and not visited[nx] :
            if nx in ladder_snake.keys() :
                nx = ladder_snake[nx]

            if not visited[nx] :
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(visited[100])