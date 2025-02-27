import sys

n = int(input())
arr = []
for _ in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

dp_max = [0] * 3
dp_max[0] = arr[0][0]
dp_max[1] = arr[0][1]
dp_max[2] = arr[0][2]

dp_min = [0] * 3
dp_min[0] = arr[0][0]
dp_min[1] = arr[0][1]
dp_min[2] = arr[0][2]

for i in range(1,n) :
    left = max(dp_max[0], dp_max[1]) + arr[i][0]
    middle = max(dp_max[0], dp_max[1], dp_max[2]) + arr[i][1]
    right = max(dp_max[1], dp_max[2]) + arr[i][2]

    dp_max[0], dp_max[1], dp_max[2] = left, middle, right

    left = min(dp_min[0], dp_min[1]) + arr[i][0]
    middle = min(dp_min[0], dp_min[1], dp_min[2]) + arr[i][1]
    right = min(dp_min[1], dp_min[2]) + arr[i][2]

    dp_min[0], dp_min[1], dp_min[2] = left, middle, right

print(max(dp_max), min(dp_min))
