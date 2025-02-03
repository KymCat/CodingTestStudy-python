import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
finds = map(int, sys.stdin.readline().split())
array = [ i for i in range(1,n+1)]

queue = deque(array)

cnt = 0
for i in finds :
    idx = queue.index(i)
    if idx > len(queue)//2 :
        while True : # 오른쪽으로 쉬프트
            value = queue.popleft()
            if value == i : break
            queue.appendleft(value)

            queue.appendleft(queue.pop())
            cnt += 1

    else :
        while True : # 왼쪽으로 쉬프트
            value = queue.popleft()
            if value == i : break
            queue.append(value)
            cnt+=1

print(cnt)