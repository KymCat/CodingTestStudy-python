import sys
n = int(input())
#
# arr = []
# for _ in range(n) :
#     arr.append(sys.stdin.readline().rstrip())
#
# def quick_sort(arr) :
#     if len(arr) <= 1  :
#         return arr
#
#     tail = arr[1:]
#     pivot = arr[0]
#     pivot_len = len(pivot)
#     left_side, right_side = [], []
#     for i in tail :
#         if len(i) == pivot_len :
#             if i > pivot :
#                 right_side.append(i)
#             else :
#                 left_side.append(i)
#
#         elif len(i) < pivot_len :
#             left_side.append(i)
#         else :
#             right_side.append(i)
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# for i in quick_sort(list(set(arr))) :
#     print(i)


arr = []

for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
arr = list(set(arr))
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)