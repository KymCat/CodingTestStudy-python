import sys

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        sums = [max(x - mid, 0) for x in arr] # x-mid와 0을 비교하여 둘 중 큰 것을 선택
        height = sum(sums)

        if height >= target :
            result = mid
            start = mid + 1
        else :
            end = mid - 1

    return result


n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

answer = binary_search(arr, m, 0, max(arr))
if answer == None :
    print("Not found")
else :
    print(answer)
