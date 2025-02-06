import sys

n = int(input())

dp = [[] for _ in range(n)]
for i in range(n) :
    dp[i] = list(map(int, sys.stdin.readline().split()))


for i in range(1,n) :
    for j in range(len(dp[i])) :
        if j == 0 :
            dp[i][j] += dp[i-1][0]

        elif j == len(dp[i]) - 1 :
            dp[i][j] += dp[i-1][j-1]

        else :
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))