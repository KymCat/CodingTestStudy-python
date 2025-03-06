import sys

INF = int(1e9)
n = int(input())
m = int(input())

city = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    city[a][b]= min(city[a][b], c)


for i in range(n+1) :
    for j in range(n+1) :
        if i == j :
            city[i][j] = 0


for k in range(1,n+1) :
    for i in range(1, n+1):
        for j in range(1, n+1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        print( 0 if city[i][j] == INF else city[i][j], end=" ")
    print()
