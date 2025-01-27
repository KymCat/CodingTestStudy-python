import sys, heapq
from collections import defaultdict

n = int(input())

q = []
abs_dict = defaultdict(int)
for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
        if not q :
            print(0)
        else :
            value = heapq.heappop(q)
            if -value in abs_dict :
                abs_dict[-value] -= 1

                if abs_dict[-value] == 0 :
                    del abs_dict[-value]

                print(-value)
            else :
                abs_dict[value] -= 1

                if abs_dict[value] == 0 :
                    del abs_dict[value]

                print(value)

    else :
        heapq.heappush(q,x if x > 0 else -x)
        abs_dict[x] += 1


# 훨씬 깔끔한 코드 - https://claude-u.tistory.com/154
# n = int(input())
# q = []
#
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     if x != 0:
#         heapq.heappush(q, (abs(x), x)) # 인덱스0의 값이 같다면 인덱스1로 다시 정렬함
#     else:
#         try:
#             print(heapq.heappop(q)[1]) # (abs(x), x) 에서 x 값을 출력
#         except:
#             print(0)