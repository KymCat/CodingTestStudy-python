import sys
from collections import defaultdict

n,m = map(int, sys.stdin.readline().split())

memo = defaultdict(str)
for _ in range(n) :
    address, pw = map(str, sys.stdin.readline().split())
    memo[address] = pw

for _ in range(m) :
    address = sys.stdin.readline().rstrip()
    print(memo[address])