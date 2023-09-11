import sys

t = int(input())
dp = [[ i for i in range(1,16) ] for _ in range(15)]
for i in range(1,15) :
    for j in range(1,15) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for _ in range(t) :
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(dp[k][n-1])