n = int(input())

dp = [1001] * 1001
dp[0] = 0
dp[1] = 3

array = [1,3]

for i in range(2) :
    for j in range(array[i], n+1) :
        dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[n] % 2 == 0 :
    print('SK')
else :
    print('CY')