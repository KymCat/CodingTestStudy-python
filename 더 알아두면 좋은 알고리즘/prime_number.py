# 소수 판별 프로그램들
import math
n = int(input())

# N이 소수인지 판별하기 위해서는 N의 제곱근까지만 나누어 떨어지는지 확인
def prime_number(n) :
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

# 에라토스테네스의 체 -> N까지의 소수 개수 출력 알고리즘
# 메모리가 많이 필요하다는 단점 존재
'''
1. 2부터 N까지의 모든 자연수를 나열한다
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾고
3. 남은 수 중에서 i의 배수를 모두 제거한다. ( 단 본인 i는 제거 X )
4. 더 이상 반복할 수 없을 때까지 2번 과 3번 과정을 반복한다.
'''

def Eratosthenes(n) :
    array = [ True for _ in range(n+1) ] # 처음에는 모두가 소수
    # array[0] = False , array[1] = False 로 해놓는 것도 좋다.

    for i in range(2, int(math.sqrt(n)) + 1) : # 이것 또한 제곱근까지 확인하면 끝난다
        if array[i] == True :
            j = 2
            while i * j <= n :
                array[i * j] = False  # i x 2 , i x 3, i x 4 ... 를 소수에서 제외
                j += 1

    count = 0
    for i in range(2, n+1) :
        if array[i] == True :
            count += 1
    return count

print(prime_number(n))
print(Eratosthenes(n))