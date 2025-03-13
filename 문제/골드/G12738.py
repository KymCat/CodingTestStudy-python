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