'''
input
5
8 3 7 9 2
3
5 7 9

out
no yes yes
'''

# 이진탐색 계수정렬 집합 으로 해결 가능
n = int(input()) # 가지고 있는 부품개수
parts = list(map(int, input().split())) # 부품들 고유 번호 입력 받기
parts.sort() # 이진 탐색으로 찾기 위해 미리 정렬

m = int(input()) # 손님이 찾을 부품 개수
find_parts = list(map(int, input().split())) # 손님이 찾을 부품 고유 번호

def binary_search(array, target, start, end) :
    if start > end :
        return False
    mid = (start + end) // 2
    if array[mid] == target :
        return True
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else :
        return binary_search(array, target, mid + 1, end)

for i in range(m) :
    if binary_search(parts, find_parts[i], 0, n-1) :
        print('yes', end = " ")
    else :
        print('no', end = " ")