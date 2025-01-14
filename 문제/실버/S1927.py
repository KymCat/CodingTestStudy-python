import sys, heapq

n = int(input())

q = []
for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
        # if len(q) == 0 :
        #     answer.append(0)
        # else : answer.append(heapq.heappop(q))
        try : print(heapq.heappop(q))
        except : print(0)

    else :
        heapq.heappush(q,x)
