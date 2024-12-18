# 선택 정렬
# 데이터 개수가 N개일떄 가장 작은 데이터를 앞으로 보내는 과정 N-1번 반복 O(N^2)
import time

array = [7,5,9,0,3,1,6,2,4,8]

start_time = time.time()
for i in range(len(array)) :
    min_index = i
    for j in range(i+1,len(array)) : # i보다 뒤에 있는 데이터중에서 가장 작은 데이터 찾기
        if array[min_index] > array[j] :
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # 스왑

end_time = time.time()
print(array)
print(f"time : {end_time - start_time:.6f}")