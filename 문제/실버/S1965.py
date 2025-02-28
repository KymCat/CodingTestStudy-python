import sys

n = int(input())
boxes = list(map(int,sys.stdin.readline().split()))

dp = [1] * n
for i in range(1,n) :
    for j in range(i-1,-1,-1) :
        if boxes[j] >= boxes[i] : continue
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))