"""
배낭 문제
-분할 가능 문제
    : 각 아이템 일부분을 분할해서 넣을 수 있다
    => 다이나믹 프로그래밍

- 0-1 배낭 문제
    : 각 아이템을 통째로 넣거나, 아예 안 넣거나 해야한다
    => 그리디 알고리즘
"""

"""
0-1 배낭 문제 간단 알고리즘
    max(
        1. 자신을 제외한 나머지 아이템으로 배낭을 채우거나
        2. 자신을 포함한 아이템으로 배낭을 채우기
    )
"""

def knapsack2_2(max_weight: int, weights: list, values: list):
    n = len(weights)

    # dp 초기화
    # 행 : 아이템 갯수 만큼
    # 열 : 최대 무게 까지
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # 다이나믹 프로그래밍 시작
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w: # i 번쨰 아이템을 넣을 수 있다면
                dp[i][w] = max(
                    dp[i - 1][w], # i 번째 아이템을 안 넣을 때의 최대가치, 즉 i - 1개의 아이템 만으로 무게 w까지 채운 경우
                    dp[i - 1][w - weights[i - 1]] + values[i - 1], # i 번째 아이템을 넣었을 경우, i의 무게를 덜어낸 가치 + i의 가치
                )
            else: # 넣을 수 없다면 가치 유지
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]

