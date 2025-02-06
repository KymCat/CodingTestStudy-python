import sys, heapq

n = int(input())
INF = int(1e9)

tree = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a,b,c = map(int,sys.stdin.readline().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

def dijkstra(start) :
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue

        for i in tree[node] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

    distance[0] = -1
    return distance

dist_1 = dijkstra(1)
max_node = dist_1.index(max(dist_1))
dist_2 = dijkstra(max_node)

print(max(dist_2))