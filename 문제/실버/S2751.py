import sys

n, *arr = map(int, sys.stdin.buffer.read().splitlines())

# def quick_sort(arr) :
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]
#     tail = arr[1:]
#
#     left_side = [ x for x in tail if pivot >= x]
#     right_side = [x for x in tail if pivot < x]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# for i in quick_sort(arr) :
for i in sorted(arr) :
    print(i)