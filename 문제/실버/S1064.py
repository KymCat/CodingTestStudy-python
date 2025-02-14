import sys,math

x1,y1,x2,y2,x3,y3 = map(int, sys.stdin.readline().split())
if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1) : # 외적 AB X AC
    print(-1.0)

else :
    ab = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    ac = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    bc = math.sqrt((x2-x3)**2 + (y2-y3)**2)

    circum1 = 2*ab + 2*ac
    circum2 = 2*ab + 2*bc
    circum3 = 2*ac + 2*bc


    max_cir = max(circum1, circum2, circum3)
    min_cir = min(circum1, circum2, circum3)

    print(max_cir - min_cir)