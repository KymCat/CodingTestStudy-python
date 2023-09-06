import sys

n = int(input())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(input())
arr_m = list(map(int, sys.stdin.readline().split()))

arr_n.sort()
for i in arr_m :
    is_find = False
    start, end = 0, n - 1
    while start <= end :
        mid = (start + end) // 2

        if arr_n[mid] == i :
            print(1)
            is_find = True
            break
        elif arr_n[mid] > i :
            end = mid - 1
        else :
            start = mid + 1

    if not is_find :
        print(0)