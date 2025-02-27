import sys

n  = int(sys.stdin.readline().rstrip())
dp = [0] * 50001
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4,n+1) :
    dp[i] = (dp[i-1] + dp[i-3]) % 1000000009

print(dp[n])