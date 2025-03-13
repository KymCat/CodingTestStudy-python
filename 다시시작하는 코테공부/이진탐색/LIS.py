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

# 이 코드는 최장 길이만 보장함 !!
# ans 안쪽 원소들은 최장 길이때의 원소가 아닐수도 있음 !
# 원소까지 구하는 코드 : https://github.com/KymCat/CodingTestStudy/blob/main/%EB%AC%B8%EC%A0%9C/%ED%94%8C%EB%9E%9C%ED%8B%B0%EB%84%98/P14003.py
