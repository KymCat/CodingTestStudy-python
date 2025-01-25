import sys

n = int(input())

array = []
for _ in range(n) :
    array.append(int(sys.stdin.readline().rstrip()))

min_cnt = 4
for i in array :
    cnt = 0
    for j in range(i,i+5) :
        if j not in array :
            cnt+=1

    min_cnt = min(min_cnt, cnt)

print(min_cnt)