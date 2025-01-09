import heapq
import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c]) # a=node b=node c=distance / a -- [c] -- > b

def Dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, node = heapq.heappop(q) # heapq -> (dist, node)
        if distance[node] < dist :
            continue

        for i in graph[node] : # i -> (node, dist)
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

Dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])