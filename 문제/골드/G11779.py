import sys, heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,cost = map(int, sys.stdin.readline().split())
    graph[a].append([b,cost]) # node, cost

depart, arrive = map(int, sys.stdin.readline().split())
distance = [1e9] * (n+1)
# route = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

q = []
distance[depart] = 0
heapq.heappush(q,(0, depart)) # cost, node
while q :
    cost, city = heapq.heappop(q)
    if cost > distance[city] : continue

    for i in graph[city] :
        dist = cost + i[1]
        if distance[i[0]] > dist :
            distance[i[0]] = dist
            parent[i[0]] = city
            # route[i[0]] = route[city] + [city]
            heapq.heappush(q,(dist, i[0]))

print(distance[arrive])
# print(len(route[arrive]) + 1)
# print(*route[arrive], arrive)

result = []
tmp = arrive
while True :
    result.append(tmp)
    if tmp == depart : break
    tmp = parent[tmp]

print(len(result))
print(*result[::-1])