"""
무한 배낭 문제
각 아이템을 무한히 사용할 수 있는 배낭 문제의 변형

- 아이템을 몇 번 썻는지가 중요한 것이 아님
- 같은 무게를 만들 수 있는 최소 비용
- 아이템 순서를 따로 관리할 필요가 없음 => 1차원 리스트 가능
"""

# 백준 1106번 호텔 (https://www.acmicpc.net/problem/1106)
import sys

INF = int(1e9)
C, N = map(int, sys.stdin.readline().split())

costs = []
customers = []
for _ in range(N):
    cost, customer = map(int, sys.stdin.readline().split())
    costs.append(cost)
    customers.append(customer)

# C명을 넘을 수도 있으므로 여유있게 => 문제에서 비용과 고객수가 100보다 작다고 했으니 100을 더함
dp = [INF] * (C + 100)
dp[0] = 0

# 무한 배낭 문제 => 1차원 리스트
for i in range(N):
    for c in range(customers[i], C + 100):
        dp[c] = min(dp[c], dp[c - customers[i]] + costs[i])

# 최소 C명 이상을 달성할 수 있는 가장 작은 비용
print(min(dp[C:]))
