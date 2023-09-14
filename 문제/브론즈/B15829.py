import sys

n = int(input())
s = sys.stdin.readline().rstrip()

result = 0
for i,d in enumerate(s) :
    result += ((ord(d) - 96) * 31**i)

print(result % 1234567891)