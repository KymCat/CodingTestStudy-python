import sys

s = sys.stdin.readline().rstrip()
boom = list(sys.stdin.readline().rstrip())
n, end = len(boom), boom[-1]

stack = []
for i in s :
    stack.append(i)
    if stack[-1] == end and stack[-n:] == boom :
        del stack[-n:]

print(''.join(stack) if stack else 'FRULA')
