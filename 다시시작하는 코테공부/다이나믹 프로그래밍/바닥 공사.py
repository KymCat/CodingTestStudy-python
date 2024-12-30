# 가로의 길이가 N, 세로의 길이 2
# 1x2, 2x1, 2x2의 덮개를 이용해 채우기

import sys

n = int(sys.stdin.readline())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1) :
    d[i] = (d[i-1] + (d[i-2] * 2)) % 796796

print(d[n])