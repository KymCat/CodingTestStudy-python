import sys
from collections import defaultdict

n = int(input())
dist = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = defaultdict(int)

def solution(mask, last) :
    if mask == (1 << n) - 1 : # 전부 방문했다면
        if dist[last][0] : # 마지막 도시에서 출발점으로 가는 다리가 있다면
            return dist[last][0] # 다리 dist값 반환
        else : # 마지막 도시에서 출발점으로 가는 다리가 없다면
            return 1e9 # 무한 반환 => 최솟값 채택되지 않게...

    if (mask, last) in dp :# 이미 계산된 DP라면
        return dp[(mask, last)]

    ans = 1e9
    for next in range(n) :
        if not (mask & (1 << next)) and dist[last][next] > 0 : # 방문하지 않고, next로 갈 수있는 다리가 있다면...
            ans = min(ans, solution(mask | (1 << next), next) + dist[last][next])

    dp[(mask, last)] = ans
    return ans


print(solution(1, 0))