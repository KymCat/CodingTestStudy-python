import sys, heapq


n = int(input())
q = []
for _ in range(n) :
    start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(q,(end, start)) #heapq -> (value, item)

end, start = heapq.heappop(q)
cnt = 1
while q :
    second_e, second_s = heapq.heappop(q)
    if end > second_s : continue

    start = second_s
    end = second_e
    cnt += 1

print(cnt)

