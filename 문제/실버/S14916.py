# dp 테이블로 진행
n = int(input())

dp = [-1] * 100001
dp[2],dp[4],dp[5] = 1,2,1


for i in range(6,n+1) :
    if dp[i-5] == -1 :
        dp[i] = dp[i-2] + 1

    elif dp[i-2] == -1 :
        dp[i] = dp[i-5] + 1

    else :
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)

print(dp[n])