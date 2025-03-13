# 가장 긴 증가하는 부분 수열(LIS)

# LIS 구현 방법
# 1. DP : 간단, 오래 걸림
# 2. 이진탐색 : 상대적 복잡, 효율적

# 이진탐색 LIS
# input
# 6
# 10 20 10 30 20 50

# output
# 4

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

def binary_search(start, end, target, ans) :
    while start <= end :
        mid = (start + end) // 2
        if ans[mid] > target :
            end = mid-1

        elif ans[mid] == target :
            return mid

        else :
            start = mid+1
    return start

ans = [arr[0]]
for i in range(1,n) :
    if ans[-1] < arr[i] :
        ans.append(arr[i])
    else :
        ans[binary_search(0, len(ans)-1, arr[i], ans)] = arr[i]

print(len(ans))

