'''
- 첫 번째 줄에 N,K가 공백으로 구분되어 입력된다 (1 <= N <= 100,000 / 0 <= k <= N)
- 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
- 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
- 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

input
5 3
1 2 5 4 3
5 5 6 6 5

output
26
'''
# ㅇ
# quick sort로 풀어보기
def quick_sort(array) :
    if len(array) <= 1 :
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [ x for x in tail if x <= pivot ]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = quick_sort(a)
b = quick_sort(b)

for i in range(k) :
    if a[i] > b[len(b) - 1 - i] : break
    a[i] , b[len(b) - 1 - i] = b[len(b) - 1 - i], a[i]

print(sum(a))