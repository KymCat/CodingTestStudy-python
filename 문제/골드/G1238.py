import sys, heapq

n,m,x = map(int, sys.stdin.readline().split())

city = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end, dist = map(int, sys.stdin.readline().split())
    city[start].append([end, dist]) # city => (node, dist)

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0, start)) # q => (dist, node)
    distance = [1e9] * (n+1)
    distance[start] = 0

    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue

        for city_node, city_dist in city[node] : # city => (node, dist)
            cost = dist + city_dist
            if distance[city_node] > cost :
                distance[city_node] = cost
                heapq.heappush(q,(cost, city_node))

    return distance

distance = dijkstra(x)

all_to_x_distance = [0] * (n+1)
for i in range(1,n+1) :
    if i == x : continue
    tmp_dist = dijkstra(i)
    distance[i] += tmp_dist[x]

print(max(distance[1:]))