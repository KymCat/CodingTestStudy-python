import sys

n,m = map(int, input().split())
castle = []

for _ in range(n) :
    castle.append(sys.stdin.readline().rstrip())

cnt_n = 0
for i in range(n) :
    if 'X' not in castle[i] :
        cnt_n+=1

cnt_m = 0
for j in range(m) :
    if 'X' not in [castle[i][j] for i in range(n)] :
        cnt_m+=1

print(max(cnt_n, cnt_m))
