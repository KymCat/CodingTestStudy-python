import sys
while True :
    stack = []
    sen = sys.stdin.readline().rstrip()
    if sen == '.' :
        break

    for s in sen :
        if s == '(' or s == '[' :
            stack.append(s)

        elif s == ')' :
            if  len(stack) > 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(s)
                break

        elif s == ']'  :
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else :
                stack.append(s)
                break

    if len(stack) == 0 :
        print('yes')
    else :
        print('no')