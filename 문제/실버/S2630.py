import sys
n = int(input())

maps = []
for _ in range(n) :
    maps.append(list(map(int, sys.stdin.readline().split())))

result = []
def cal_square(x,y,n) :
    color = maps[x][y]

    for i in range(x,x+n) :
        for j in range(y,y+n):
            if maps[i][j] != color :
                cal_square(x, y, n // 2)
                cal_square(x, y+(n//2), n // 2)
                cal_square(x+(n//2), y, n // 2)
                cal_square(x+(n//2), y+(n//2), n // 2)
                return

    if color == 1 :
        result.append(1)
    else : result.append(0)

cal_square(0,0,n)
print(result.count(0))
print(result.count(1))