import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
rv_arr = arr[::-1] # reverse arr..

dp_i = [1] * len(arr) # increase
dp_d = [1] * len(arr) # decrease

for i in range(n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp_i[i] = max(dp_i[i], dp_i[j]+1)

        if rv_arr[j] < rv_arr[i] :
            dp_d[i] = max(dp_d[i], dp_d[j]+1)

ans = 0
for i in range(n) :
    ans = max(ans, dp_i[i] + dp_d[n-i-1])

print(ans-1) # 자기자신 두번 더한 경우를 한번 차감