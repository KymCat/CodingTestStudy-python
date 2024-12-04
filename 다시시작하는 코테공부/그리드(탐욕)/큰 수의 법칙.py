import sys
n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()
big = data[n-1]
big_second = data[n-2]

answer = 0
count = 0
for i in range(m) :
    if count == 3 :
        answer += big_second
        count = 0
        continue
    answer += big
    count += 1

print(answer)

# 해설

answer = 0
while True :
    for i in range(k) :
        if m == 0:
            break
        answer += big
        m -= 1

    if m == 0 :
        break
    answer += big_second
    m-=1

print(answer)

# 5 8 3         : input
# 2 4 5 4 6     : input
# 46            : answer