# 0 ~ 10(컴퓨터 개수)을 각 제곱하여 10으로 나누면 규칙이보임
# 0은 제곱하고 10으로 나눠도 같기때문에 10번 컴퓨터로 처리해야함
# 1 -> 1
# 2 -> 2,4,8,6 (2**1%10, 2**2%10, 2**3%10, 2**4%10) 2**6 부터 계속 반복
# 3 -> 3,9,7,1
# 4 -> 4,6
# 5 -> 5
# 6 -> 6
# 7 -> 7,9,3,1
# 8 -> 8,4,2,6
# 9 -> 9,1

import sys

t = int(input())

for _ in range(t) :
    a,b = map(int, sys.stdin.readline().split())
    a%=10

    if a == 0 :
        print(10)
    elif a == 1 or a == 5 or a == 6 :
        print(a)
    elif a == 4 or a == 9 :
        if b % 2 == 0 :
            print((a**2)%10)
        else :
            print(a)
    else :
        if b % 4 == 0 :
            print((a**4)%10)
        elif b % 4 == 3 :
            print((a**3)%10)
        elif b % 4 == 2 :
            print((a**2)%10)

        else :
            print(a)
