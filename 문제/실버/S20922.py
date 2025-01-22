import sys
from collections import defaultdict

n,k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

i = 0
cnt = 0
max_cnt = 0
num_dict = defaultdict(int)
for j in range(n) :
    num_dict[num[j]] += 1
    cnt += 1

    while num_dict[num[j]] > k :
        num_dict[num[i]] -= 1
        cnt-=1
        i+=1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)