import sys
from collections import defaultdict


t = int(input())
for _ in range(t) :
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n) :
        name,types = map(str,sys.stdin.readline().split())
        clothes[types]+=1

    result = 1
    for i in clothes.values() :
        result *= (i+1) # + 1 은 그 옷종류를 안입는 경우를 포함하기 때문

    print(result-1) # -1은 알몸일 경우를 제외한

