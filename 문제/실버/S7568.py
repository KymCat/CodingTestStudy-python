import sys

n = int(input())
table = []
for _ in range(n) :
    x,y = map(int, sys.stdin.readline().split())
    table.append((x,y))

for i in table :
    score = 1
    for j in table :
        if i[0] < j[0] and i[1] < j[1] :
            score+=1

    print(score, end=" ")
