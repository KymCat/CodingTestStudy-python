import sys, heapq

t = int(input())

for _ in range(t) :
    k = int(input())

    min_heap = []
    max_heap = []
    deleted = [False] * k # 파이썬 힙의 디폴트는 최소힙이다.

    for i in range(k) :
        order, n = map(str, sys.stdin.readline().split())

        if order == 'I' :
            heapq.heappush(min_heap,(int(n), i)) # deleted 에서 사용할 i
            heapq.heappush(max_heap, (-int(n), i)) # -를 붙이는 것으로 최대힙 효과 / 나중에 값을 pop하고 -를 붙여줘야함.

        elif order == 'D' :
            if n == '1' : # 최댓값 삭제
                while max_heap and deleted[max_heap[0][1]] : # max_heap[0][1] -> i (True or False)
                    heapq.heappop(max_heap) # 최소 힙에선 삭제 되었는데 최대 힙에선 삭제 안된 것이 있을수도 있기에 while문으로 반복 삭제

                if max_heap : # 비어있지 않다면, ( 이 라인이 D 1을 정말 수행하는 코드임 )
                    value, key = heapq.heappop(max_heap) # (n,i)
                    deleted[key] = True # 삭제했으니 True

            else : # 최솟값 삭제
                while min_heap and deleted[min_heap[0][1]] :
                    heapq.heappop(min_heap) # 최대 힙에선 삭제 되었는데 최소 힙에선 삭제 안된 것이 있을수도 있기에 while문으로 반복 삭제

                if min_heap :
                    value, key = heapq.heappop(min_heap)
                    deleted[key] = True

    while max_heap and deleted[max_heap[0][1]]:  # 마지막으로 서로서로 삭제안된 데이터 삭제
        heapq.heappop(max_heap)

    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap : # 어차피 min_heap도 개수가 같으니 하나만 조건식에 넣음
        print(-max_heap[0][0], min_heap[0][0])
    else : print('EMPTY')