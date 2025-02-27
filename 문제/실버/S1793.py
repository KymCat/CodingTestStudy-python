import sys

arr = []
while True :
    try :
        arr.append(int(sys.stdin.readline().rstrip()))
    except :
        break

dp = [0] * 251
dp[0] = 1 # 타일을 채우는 방법이라고 했으니 dp[0]은 그 상태 자체가 타일을 채운것.. 따라서 1
dp[1] = 1
dp[2] = 3
for i in range(3,251) :
    dp[i] = dp[i-1] + (dp[i-2] * 2)

for i in arr :
    print(dp[i])