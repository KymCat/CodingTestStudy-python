from collections import deque

n,k = map(int,input().split())
q = deque( i for i in range(1,n+1))

result = []
while q :
    for i in range(0,k-1) :
        q.append(q.popleft())
    result.append(str(q.popleft()))

print('<' + ', '.join(result) + '>')