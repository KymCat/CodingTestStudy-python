import sys

n,m = map(int,sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
sum_array = [0] * (n+1)
for x in range(1,n+1) :
    sum_array[x] = sum_array[x-1] + array[x-1]


result = []
for _ in range(m) :
    i,j = map(int,sys.stdin.readline().split())
    print(sum_array[j] - sum_array[i-1])