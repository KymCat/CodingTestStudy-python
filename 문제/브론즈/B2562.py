import sys

arr = []
for _ in range(9) :
    arr.append(int(sys.stdin.readline()))

result = max(arr)
print(result)
print(arr.index(result) + 1)