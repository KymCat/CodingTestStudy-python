import sys

n = int(input())


maps = list(map(int, sys.stdin.readline().split()))
min_dp = maps
max_dp = maps
for i in range(n-1) :
    maps = list(map(int, sys.stdin.readline().split()))
    min_dp = [maps[0] + min(min_dp[0], min_dp[1]), maps[1] + min(min_dp), maps[2] + min(min_dp[1], min_dp[2])]
    max_dp = [maps[0] + max(max_dp[0], max_dp[1]), maps[1] + max(max_dp), maps[2] + max(max_dp[1], max_dp[2])]

print(max(max_dp), min(min_dp))