import sys

n = int(input())
A,B,C,D,E,F = map(int, sys.stdin.readline().split())


if n >= 2 :
    # 내가 처음 제출한 코드
    # cb_side3_min = min(
    #     A+B+C, A+C+E, A+B+D, A+D+E,
    #     F+B+C, F+C+E, F+B+D, F+D+E )
    #
    # cb_side2_min = min(
    #     A+B, A+D, A+C, A+E, F+B, F+D, F+C, F+E, D+E, D+B, B+C, C+E )
    #
    # cb_side1_min = min(A,B,C,D,E,F)

    # 다른 사람이 제출한 코드 공부
    # 각 마주 보는 변 중 가장 작은거 넣기
    min_list = []
    min_list.append(min(A,F))
    min_list.append(min(C,D))
    min_list.append(min(B,E))
    min_list.sort()

    cb_side1_min = min_list[0]
    cb_side2_min = cb_side1_min + min_list[1]
    cb_side3_min = cb_side2_min + min_list[2]

    side3 = 4
    side2 = 8*(n-2) + 4
    side1 = 5*(n**2) - (3 * side3 + 2 * side2)

    side3_sum = side3 * cb_side3_min
    side2_sum = side2 * cb_side2_min
    side1_sum = side1 * cb_side1_min

    print(side3_sum + side1_sum + side2_sum)

else :
    print(sum([A,B,C,D,E,F]) - max(A,B,C,D,E,F))

