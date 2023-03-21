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

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수
n,m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [ [] for _ in range(n+1)] # n+1을 하는 이유는 각 노드에 숫자에 맞게 할당하기 위해서
# 방문한 적 있는지 체크하는 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선에 대한 정보 입력받기
for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node() :
    min_value = INF
    index = 0
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i

    return index

def dijkstra(start) :

    distance[start] = 0
    visited[start] = True
    for i in graph[start] :
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1) :
        index = get_smallest_node()
        visited[index] = True


        for j in graph[index] :
            cost = distance[index] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else : print(distance[i])

'''
시간 복잡도 O(v^2) 단, v는 노드 개수
전체 노드의 수가 5천개 이하라면 일반적으로 이 코드로 해결 가능
하지만, 노드 개수가 1만개를 넘어서면 이 코드로는 문제 해결이 어렵다.
'''