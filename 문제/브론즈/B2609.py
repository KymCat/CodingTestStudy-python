import sys, math
n = list(map(int, sys.stdin.readline().split()))

print(math.gcd(*n), math.lcm(*n))