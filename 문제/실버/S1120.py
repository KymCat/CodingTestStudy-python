import sys

a,b= map(str, sys.stdin.readline().split())

len_a = len(a)
answer = 1e9
for i in range(0,len(b)-len_a + 1) :
    cnt = 0

    slice_b = b[i:i+len_a]
    for j in range(len(a)) :
        if a[j] != slice_b[j] : cnt+=1

    answer = min(answer, cnt)

print(answer)