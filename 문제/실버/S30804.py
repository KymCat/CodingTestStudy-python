import sys
from collections import defaultdict

n = int(input())
fruit = list(map(int, sys.stdin.readline().split()))

i = 0
max_cnt = 0
fruit_dict = defaultdict(int)
for j in range(n) :
    fruit_dict[fruit[j]] += 1

    while len(fruit_dict) > 2 :
        fruit_dict[fruit[i]] -= 1
        if fruit_dict[fruit[i]] == 0 :
            del fruit_dict[fruit[i]]
        i+=1

    max_cnt = max(max_cnt, sum(fruit_dict.values()))

print(max_cnt)

