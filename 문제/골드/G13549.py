import sys, heapq


INF = int(1e9)
n,k = map(int, sys.stdin.readline().split())
distance = [INF] * 100_001

def solution(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, x = heapq.heappop(q)  # heapq -> (dist, node)
        if distance[x] < time:
            continue

        dx = [x-1, x+1, 2*x]
        for i in range(3):  # i -> (node, dist)
            if 0 <= dx[i] < 100_001 :
                cost = time
                if i != 2 : cost+=1

                if cost < distance[dx[i]] :
                    distance[dx[i]] = cost
                    heapq.heappush(q,(cost, dx[i]))

    return distance[k]

print(solution(n))