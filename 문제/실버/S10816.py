import sys
from collections import Counter

# 원래 .count() 로 쓸려고 했는데 시간초과로 Counter을 씀

n = int(input())
arr_n  = list(map(int, sys.stdin.readline().split()))

m = int(input())
arr_m = list(map(int, sys.stdin.readline().split()))

dic = dict(Counter(arr_n))
for i in arr_m :
    print(dic.get(i,0), end =" ")