# 입력 조건1 : 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다
# 입력 조건2 : 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1이상 100,000이하의 자연수이다.

# 출력 조건 : 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다, 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

# 입력예시
# 3
# 15
# 27
# 12

# 출력예시
# 27 15 12

import sys
import copy

n = int(sys.stdin.readline())
array = []
for _ in range(n) :
    array.append(int(sys.stdin.readline()))

array_insert = copy.deepcopy(array) # 삽입 정렬에 사용할 리스트
array_select = copy.deepcopy(array) # 선택 정렬에 사용할 리스트

# .sort() 내장함수 사용
array.sort(reverse=True)
for i in array :
    print(i, end=" ")

print()

# 삽입정렬 사용

for i in range(1,len(array_insert)) :
    for j in range(i,0,-1) :
        if array_insert[j] > array_insert[j-1] :
            array_insert[j], array_insert[j-1] = array_insert[j-1], array_insert[j]
        else :
            break

for i in array_insert :
    print(i, end=" ")

print()

# 선택정렬 사용
for i in range(len(array_select)) :
    max_index = i
    for j in range(i+1,len(array_select)) :
        if array_select[i] < array_select[j] :
            max_index = j

    array_select[i], array_select[max_index] = array_select[max_index], array_select[i]

for i in array_select :
    print(i, end=" ")