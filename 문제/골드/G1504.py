import sys, heapq

n,e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(e) :
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c]) # graph -> (node, dist)
    graph[b].append([a,c])

v1, v2 = map(int, sys.stdin.readline().split())
def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start)) # heapq -> (dist, node)
    distance = [1e9] * (n + 1)
    distance[start] = 0

    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue

        for i in graph[node] : # graph -> (node, dist)
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


    return distance

distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# 1 -> v1 -> v2 -> n / 1 -> v2 -> v1 -> n 중 작은가중치 택1
answer = min(distance[v1] + v1_distance[v2] + v2_distance[n], distance[v2] + v2_distance[v1] + v1_distance[n])
if answer >= 1e9 :
    print(-1)
else : print(answer)
