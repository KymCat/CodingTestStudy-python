import sys

def binary_search(arr, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

n, target = map(int, sys.stdin.readline().split()) # n : 리스트 원소수, target : 찾을 원소
arr = list(map(int, sys.stdin.readline().split()))

result = binary_search(arr, target,0, n-1)
if result == None :
    print("target not found")
else :
    print(f"target found at {result + 1}")