import copy
import sys, heapq

tc = int(input())
INF = int(1e9)

for _ in range(tc) :
    n,m,w = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(m) :
        s,e,t = map(int, sys.stdin.readline().split())
        graph.append((s,e,t))
        graph.append((e,s,t))

    for _ in range(w) :
        s,e,t = map(int, sys.stdin.readline().split())
        graph.append((s,e,-t))
    def bf(start):
        distance = [INF] * (n+1)
        distance[start] = 0

        for i in range(n) :
            for a, b, dist in graph :
                if distance[b] > dist + distance[a] :
                    distance[b] = dist + distance[a]

                    if i == n-1 :
                        return True
        return False

    if bf(1) :
        print('YES')
    else : print('NO')