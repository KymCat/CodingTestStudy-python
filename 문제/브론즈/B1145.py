# arr = list(map(int, input().split()))
# start = min(arr)
#
# while True :
#     count = 0
#     for num in arr :
#         if start % num == 0 :
#             count += 1
#     if count >= 3 :
#         break
#     else :
#         start += 1
#
# print(start)
# 위 코드는 시간이 너무 오래걸림 => 468ms

# 3개의 조합을 이용하여 최소공배수 중 가장 작은 것 찾기
import itertools
import math

arr = list(map(int, input().split()))
arr_cb = list(itertools.combinations(arr, 3))

result = []
for data in arr_cb :
    result.append(math.lcm(*data))

print(min(result))
# 40ms


