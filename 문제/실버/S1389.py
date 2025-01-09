import sys

INF = int(1e9)
n,m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if i == j:
                graph[i][j] = 0
            else :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 1
answer_sum = sum(graph[1])
for i in range(2,n+1) :
    if answer_sum > sum(graph[i]) :
        answer = i
        answer_sum = sum(graph[i])

print(answer)