import math
import sys
def solution(n) :
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in arr :
    if i == 1 :
        continue
    if solution(i) :
        cnt+=1

print(cnt)