import sys

n = int(input())

arr = []
for _ in range(n) :
    x,y = map(int, sys.stdin.readline().split())
    arr.append([x,y])

# 신발끈 공식
area = 0
for i in range(n) :
    x1,y1 = arr[i]
    x2,y2 = arr[(i+1) % n]
    area += (x1 * y2) - (x2 * y1)

print(round(abs(area / 2), 1))
