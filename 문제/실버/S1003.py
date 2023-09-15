import sys
n = int(sys.stdin.readline())
dp_0 = [1] * 41
dp_1 = [1] * 41
dp_0[1], dp_1[0] = 0,0

for i in range(2,41) :
    dp_0[i] = dp_0[i-1] + dp_0[i-2]
    dp_1[i] = dp_1[i - 1] + dp_1[i - 2]

for _ in range(n) :
    t = int(sys.stdin.readline())
    print(dp_0[t], dp_1[t])
