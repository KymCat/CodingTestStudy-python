import sys
import math

t = int(input())
for _ in range(t) :
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 두 원이 완전히 겹칠때
    if r1 == r2 and distance == 0 :
        print(-1)

    # 원이 서로 다른 두 점에서 만날때
    elif abs(r1 - r2) < distance < r1 + r2 :
        print(2)

    # 원이 내접 외접 할때
    elif abs(r1-r2) == distance or r1 + r2 == distance :
        print(1)

    else :
        print(0)