import sys

t = int(input())

for _ in range(t) :
    n = int(input())
    coins = [0]+ list(map(int, sys.stdin.readline().split()))
    m = int(input())

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,n+1) :
        dp[i][coins[i]] += 1

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if coins[i] >= j :
                dp[i][j] += dp[i-1][j]
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp[n][m])
