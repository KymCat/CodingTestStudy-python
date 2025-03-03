import sys

n,m  = map(int, sys.stdin.readline().split())
customer = []
for _ in range(m) :
    customer.append(int(sys.stdin.readline().rstrip()))


customer.sort()
ans = customer[0] * m
price = customer[0]
for i in range(1,m) :
    sum = 0
    buy = 0
    for j in range(i,m) :
        if buy == n : break
        sum += customer[i]
        buy+=1
    if ans < sum :
        price = customer[i]
    ans = max(ans, sum)


print(price, ans)
