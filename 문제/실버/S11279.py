import sys, heapq

n = int(input())

q = []
for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x > 0 :
        heapq.heappush(q,-x)
    else :
        if q :
            value = heapq.heappop(q)
            print(-value)
        else :
            print(0)
