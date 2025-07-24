import sys

INF = int(1e9)
C, N = map(int, sys.stdin.readline().split())

costs = []
customers = []
for _ in range(N):
    cost, customer = map(int, sys.stdin.readline().split())
    costs.append(cost)
    customers.append(customer)


dp = [INF] * (C + 100)
dp[0] = 0

# 무한 배낭 문제 => 1차원 리스트
for i in range(N):
    for c in range(customers[i], C + 100):
        dp[c] = min(dp[c], dp[c - customers[i]] + costs[i])

print(min(dp[C:]))
