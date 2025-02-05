import sys, heapq

n = int(input())
m = int(input())
INF = int(1e9)

bus = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end, dist = map(int, sys.stdin.readline().split())
    bus[start].append([end,dist])

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start, end) :
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist : continue

        for i in bus[node] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


    return distance[end]

print(dijkstra(start, end))