from math import factorial
t = int(input())
for _ in range(t) :
    n,m = map(int, input().split())
    print(factorial(m) // (factorial(m-n) * factorial(n)))

# --------- 다이나믹 해결법
# n과 m이 30까지임
t = int(input())
dp = [ [0]*30 for _ in range(30) ]

for i in range(30) :
    for j in range(30) :
        if i == 1 :
            dp[i][j] = j
        else :
            if i == j :
                dp[i][j] = 1
            elif i < j :
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(t) :
    n,m = map(int, input().split())
    print(dp[n][m])

