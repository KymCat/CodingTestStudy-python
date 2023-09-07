import sys
from collections import Counter

n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(round(sum(arr)/n))
print(arr[len(arr)//2])

dic = dict(Counter(arr).most_common())
max_cnt = max(dic.values())
if list(dic.values()).count(max_cnt) > 1 :
    print(list(dic.keys())[1])
else :
    print(list(dic.keys())[0])

print(arr[n-1] - arr[0])
