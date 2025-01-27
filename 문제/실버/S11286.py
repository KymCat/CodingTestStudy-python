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