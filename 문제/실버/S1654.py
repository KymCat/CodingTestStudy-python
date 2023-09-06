import sys
k,n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1,max(lan)

while start <= end :
    mid = (start + end) // 2

    cnt = 0
    for i in lan :
        cnt = cnt + (i//mid)

    if cnt >= n : # n보다 큰데 왜 start를 mid + 1을 하는 이유
        start = mid + 1 # cnt 수가 많아진다는 것은 n개를 만들 수 있는 랜선의 최대길이가 작다는것
    else :
        end = mid - 1

print(end)
