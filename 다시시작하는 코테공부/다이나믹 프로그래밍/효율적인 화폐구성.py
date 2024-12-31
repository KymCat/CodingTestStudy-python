# 화폐에서 큰 단위가 작은 단위의 배수면 그리디로 해결이 가능, 하지만 아닐 경우에는 다이나믹 프로그래밍으로 해결해야함
import sys

n,m = map(int,sys.stdin.readline().split())
array = []
for _ in range(n) :
    array.append(int(sys.stdin.readline()))

d = [10001] * (m+1)
d[0] = 0 #d[j - array[i]]가 d[0]가 되었을 때(자기자신) +1을 하기위함

for i in range(n) : # 화폐 개수만큼 반복
    for j in range(array[i], m+1) : # array[i]는 화폐 종류가 삽입되어있음
        d[j] = min(d[j], d[j-array[i]] + 1)


if d[m] != 10001 :
    print(d[m])
else :
    print(-1)



