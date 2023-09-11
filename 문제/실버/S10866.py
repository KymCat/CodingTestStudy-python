import sys
from collections import deque

n = int(input())
stack = deque()
for _ in range(n) :
    order = sys.stdin.readline().rstrip().split()
    if len(order) > 1 :
        if order[0] == 'push_back' :
            stack.append(order[1])
        else :
            stack.appendleft(order[1])

    else :
        if order[0] == 'pop_front' :
            print(-1 if len(stack) == 0 else stack.popleft())
        elif order[0] == 'pop_back' :
            print(-1 if len(stack) == 0 else stack.pop())
        elif order[0] == 'size' :
            print(len(stack))
        elif order[0] == 'empty' :
            print( 1 if len(stack) == 0 else 0)
        elif order[0] == 'front' :
            print( -1 if len(stack) == 0 else stack[0])
        else :
            print(-1 if len(stack) == 0 else stack[len(stack)-1])