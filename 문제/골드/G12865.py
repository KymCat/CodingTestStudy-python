import sys

n,k = map(int, sys.stdin.readline().split())
dp = [[0] * (k+1) for _ in range(n+1)]

weight = [0]
value = [0]
for _ in range(n) :
    w,v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

for i in range(1,n+1) :
    for j in range(1,k+1) :
        if weight[i] > j :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

print(dp[n][k])