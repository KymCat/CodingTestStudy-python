import sys

n = int(input())
stack = []
for _ in range(n) :
    order = sys.stdin.readline().rstrip().split()
    if len(order) > 1 :
        stack.append(order[1])

    else :
        if order[0] == 'pop' :
            print(-1 if len(stack) == 0 else stack.pop())
        elif order[0] == 'size' :
            print(len(stack))
        elif order[0] == 'empty' :
            print( 1 if len(stack) == 0 else 0)
        else :
            print(-1 if len(stack) == 0 else stack[len(stack)-1])