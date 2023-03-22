'''
input       output      첫째 줄 : 노드의 개수, 간선의 개수
6 11        0           둘째 줄 : 시작 노드 번호
1           2           세번째 줄부터 : 각 노드에 연결되어 있는 노드에 대한 정보
1 2 2       3           (1 2 2) : 1번 노드에서 2번 노드로 가는 비용이 2라는 의미
1 3 5       1
1 4 1       2
2 3 3       4
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [ [] for _ in range(n+1)] # n+1을 하는 이유는 각 노드에 숫자에 맞게 할당하기 위해서
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선에 대한 정보 입력받기
for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0

    while q :
        # 가장 우선순위가 높은(거리가 짧은) 데이터를 POP
        dist, node = heapq.heappop(q)

        # 이미 방문한 노드면 continue
        if distance[node] < dist :
            continue

        for i in graph[node] :
            cost = distance[node] + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                # 연결된 노드 정보 PUSH
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n + 1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])

'''
시간 복잡도 O(E * logV) 단, E는 간선의 개수 V는 노드의 개수
'''