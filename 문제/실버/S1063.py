import sys

move = {
    # key : [x,y]
    'R' : [0, 1],
    'L' : [0,-1],
    'B' : [-1,0],
    'T' : [1,0],
    'RT':[1,1],
    'LT':[1,-1],
    'RB':[-1,1],
    'LB':[-1,-1]
}

king, rock, n = sys.stdin.readline().split()
# 리스트 좌표로 변환
kx, ky = int(king[1])-1, ord(king[0])-ord('A')
rx, ry =  int(rock[1])-1, ord(rock[0])-ord('A')
n = int(n)



orders = []
for _ in range(n) :
    orders.append(sys.stdin.readline().rstrip())

for order in orders :
    x,y = move.get(order)

    # 킹
    kdx = kx + x
    kdy = ky + y
    if 0 <= kdx < 8 and 0 <= kdy < 8 :

        # 킹 이동할 위치 == 돌 위치
        if rx == kdx and ry == kdy :
            rdx = rx + x
            rdy = ry + y
            if 0 <= rdx < 8 and 0 <= rdy < 8:
                rx,ry = rdx, rdy
                kx, ky = kdx, kdy

        else :
            kx, ky = kdx, kdy


print(chr(ky + ord('A')) + str(kx+1))
print(chr(ry + ord('A')) + str(rx+1))


