import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())

house = []
chicken = []
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n) :
        if row[j] == 1 :
            house.append([i,j])
        elif row[j] == 2 :
            chicken.append([i,j])

ans = 1e9
for cb in list(combinations(chicken, m)) : # 치킨집 좌표중 m개 뽑, 순서고려X
    # cb => [(x1,y1), (x2, y2) ... (xm, ym)]

    sum_dist = 0
    for i in range(len(house)) :
        min_dist = 1e9
        for x,y in cb :
            min_dist = min(min_dist, abs(house[i][0] - x) + abs(house[i][1] - y))
        sum_dist += min_dist

    ans = min(ans, sum_dist)

print(ans)



# 처음 풀어본 방법
# 그런데 너무 복잡하고 내 스타일이 아니라서 최적화 시도
# 속도는 이게 더 빠름
# distance = [[0] * len(house) for _ in range(len(chicken))]
#
# for i in range(len(chicken)) :
#     for j in range(len(house)) :
#         distance[i][j] = abs(house[j][0] - chicken[i][0]) + abs(house[j][1] - chicken[i][1])
#
# cb = list(combinations([i for i in range(len(chicken))], m))
#
# ans = 1e9
# for x in cb :
#     distance_cb = []
#     for row in x :
#         distance_cb.append(distance[row])
#
#     sum = 0
#     for i in range(len(distance_cb[0])) :
#         dist_min = 1e9
#         for j in range(len(distance_cb)) :
#             dist_min = min(dist_min, distance_cb[j][i])
#         sum += dist_min
#
#     ans = min(ans, sum)
# print(ans)