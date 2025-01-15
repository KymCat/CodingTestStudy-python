import sys

n = int(input())
stair = []
stair.append(0)

for _ in range(n) :
    stair.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (n+1)
if n > 1 :
    dp[1] = stair[1]
    dp[2] = stair[2] + dp[1]

    for i in range(3,n+1) :
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]
else :
    dp[1] = stair[1]
print(dp[n])