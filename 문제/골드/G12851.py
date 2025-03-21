import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
m =  n if n >= k else k

maps = [0] * (2*m) # count
times = [1e9] * (2*m) # time
def bfs(start) :
    q = deque([(start, 0)]) # location, time
    maps[start] = 1
    times[start] = 0

    while q :
        cur, time = q.popleft()

        for i in [cur+1, cur-1, cur*2] :
            if 0 <= i < 2*m and times[i] >= time + 1 :
                if times[i] == time + 1 :
                    maps[i] +=1

                elif times[i] > time + 1 :
                    times[i] = time + 1
                    maps[i] = 1
                q.append((i, time + 1))
bfs(n)
print(times[k])
print(maps[k])
