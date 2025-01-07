n = int(input())

dp = [-1] * 81
dp[0] = 0
dp[1], dp[2] = 1,1

for i in range(3,n+1) :
    dp[i] = dp[i-1] + dp[i-2]

answer = (dp[n] * 2) + (dp[n] + dp[n-1])*2
print(answer)