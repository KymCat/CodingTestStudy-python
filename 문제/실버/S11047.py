import sys

n,k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n) :
    coins.append(int(sys.stdin.readline().rstrip()))


cnt = 0

for coin in reversed(coins) :
    if k < coin :  continue
    cnt += k // coin
    k %= coin

print(cnt)