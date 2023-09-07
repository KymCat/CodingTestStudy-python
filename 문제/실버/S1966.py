import sys
from collections import deque

t = int(input())
for _ in range(t) :
    n,m = map(int, sys.stdin.readline().split())
    imp = deque(list(map(int, sys.stdin.readline().split())))
    count = 0

    while imp :
        max_data = max(imp)
        data = imp.popleft()
        m -= 1

        if max_data == data :
            count+=1
            if m < 0 : # m이 0보다 작다는 것 : pop된게 m이라는 것
                print(count)
                break

        else :
            imp.append(data)
            if m < 0 :
                m = len(imp) -1





