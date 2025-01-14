from collections import deque

n,k = map(int, input().split())
INF = 100001
def bfs(start) :
    queue = deque([start])

    visited = [0] * INF
    while queue :
        x = queue.popleft()
        if x == k :
            print(visited[x])
            break

        for i in (x+1, x-1, x*2) :
            if 0 <= i <= INF-1 and not visited[i] :
                visited[i] = visited[x] + 1
                queue.append(i)

bfs(n)