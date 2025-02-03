import sys


t = int(input())
for _ in range(t) :
    x1,y1, x2,y2 = map(int, sys.stdin.readline().split())
    aff1 = set()
    aff2 = set()

    n = int(input())
    for i in range(n) :
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (x1 - cx)**2 + (y1 - cy)**2 < r**2 :
            aff1.add(i)

        if (x2 - cx)**2 + (y2 - cy)**2 < r**2 :
            aff2.add(i)

    intersection = aff1 & aff2 # 같은 행성계에 속해 있다면 그 행성계는 제외
    aff1 -= intersection
    aff2 -= intersection

    print(len(aff1) + len(aff2))