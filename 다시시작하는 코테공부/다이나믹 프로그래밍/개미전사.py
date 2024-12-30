import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

d = [0] * 100

d[0] = array[0] # 인덱스 0이 첫번째 창고를 털었을때를 말하는듯 ...
d[1] = max(array[0], array[1])

for i in range(2,n) :
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
print(d[:5])