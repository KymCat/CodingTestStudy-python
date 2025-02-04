import sys
INF = int(1e9)

n,m = map(int, sys.stdin.readline().split())
graph = []
distance = [INF] * (n+1)

for _ in range(n+1) :
    a,b,c = map(int, sys.stdin.readline().split())
    graph.append((a,b,c)) # a -- (c) -- > b / start, end, dist

def bf(start) :
    distance[start] = 0

    for i in range(n) : # n-1 번 반복
        for j in range(m) : # 모든 간선 확인
            start, end, dist = graph[j][0], graph[j][1], graph[j][2]

            if distance[start] != INF and distance[end] > dist + distance[start] :
                distance[end] = dist + distance[start]

                if i == n-1 : # 음의 간선 순환 발생 / i가 증가해도 계속 갱신된다는 뜻임
                    return True
    return False

negative_cycle = bf(1)
if negative_cycle :
    print(-1)
else :
    for i in range(2, n+1) :
        if distance[i] == INF :
            print(-1)
        else :
            print(distance[i])