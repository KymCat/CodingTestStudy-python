import sys, bisect

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

ans = [arr[0]]
record = [0] * n
for i in range(n) :
    if ans[-1] < arr[i] :
        ans.append(arr[i])
        record[i] = len(ans) - 1

    else :
        idx = bisect.bisect_left(ans, arr[i])
        ans[idx] = arr[i]
        record[i] = idx

print(len(ans))
max_record = max(record)

result = []
for i in range(len(record)-1, -1, -1) :
    if record[i] == max_record :
        result.append(arr[i])
        max_record-=1

print(*result[::-1])

