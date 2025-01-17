import sys

t = int(input())
array = []
for _ in range(t) :
    array.append(int(sys.stdin.readline().rstrip()))

dp = [0] * 11
dp[1] = 1 # 1
dp[2] = 2 # 1+1 / 2
dp[3] = 4 # 1+1+1 / 1+2 / 2+1 / 3

for i in range(4,11) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in array :
    print(dp[i])