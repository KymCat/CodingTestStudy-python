import sys

n,m = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n) :
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

max_ans = 1
for x in range(n) :
    for y in range(m) :
        i = 1
        while 0 <= x+i < n and 0 <= y+i < m :
            if maps[x][y+i] == maps[x+i][y] == maps[x+i][y+i] == maps[x][y] :
                max_ans = max(max_ans, (i+1)**2)
            i+=1

print(max_ans)
