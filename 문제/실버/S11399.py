import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
array = sorted(array)

answer = 0
for i in range(n) :
    # answer += array[i] + sum(array[:i])
    answer += array.pop() * (i+1)

print(answer)