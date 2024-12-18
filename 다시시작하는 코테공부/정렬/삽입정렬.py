# 삽입정렬
# 데이터를 하나씩 확인하여 각 데이터를 적절한 위치에 삽입
# 데이터가 어느정도 정렬이 되어있으면 퀵정렬보다 효과적 O(N^2), 최선의 경우 O(N)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]

        else : break

print(array)