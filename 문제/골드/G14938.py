import sys, heapq

n,m,r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))

maps = [[] for _ in range(n+1)]
for _ in range(r) :
    a,b,c = map(int, sys.stdin.readline().split())
    maps[a].append([b,c])
    maps[b].append([a,c])

def Dijkstra(start) :
    q = []
    heapq.heappush(q,(0, start))
    distance = [1e9] * (n+1)
    distance[start] = 0

    while q :
        cost, node = heapq.heappop(q)
        if distance[node] < cost : continue

        for next, n_cost in maps[node] :
            dist = n_cost + cost
            if dist > m : continue
            elif distance[next] > dist :
                distance[next] = dist
                heapq.heappush(q,(dist, next))
    return sum(item[idx] for idx,value in enumerate(distance) if value < 1e9)

ans = 0
for i in range(1,n+1) :
    ans = max(ans, Dijkstra(i))
print(ans)