import sys

k = int(input())

stack = []
for _ in range(k) :
    n = int(sys.stdin.readline())
    if n == 0 :
        stack.pop()
        continue
    stack.append(n)

print(sum(stack))

