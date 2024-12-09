# 정수 N입력시, 00:00:00 ~ N:59:59까지 3이 하나라도 포함되면 카운트
import sys

n = int(sys.stdin.readline())

count = 0
for i in range(n+1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                count+=1

print(count)