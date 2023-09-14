import sys

# 계수 정렬
n = int(sys.stdin.readline())
cnt_sort = [0] * 10001

for _ in range(n) :
    cnt_sort[int(sys.stdin.readline())]+=1

for i in range(10001) :
    if cnt_sort[i] != 0 :
        for j in range(cnt_sort[i]) :
            print(i)