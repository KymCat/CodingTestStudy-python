import sys

equation = sys.stdin.readline().rstrip()

stack = []
answer = ''
for i in equation :
    if i.isalpha() :
        answer += i
    else :
        if i == '(' :
            stack.append(i)

        elif i == '+' or i == '-' :
            while stack and stack[-1] != '(' :
                answer+=stack.pop()
            stack.append(i)

        elif i == '*' or i == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                answer+=stack.pop()
            stack.append(i)

        elif i == ')' :
            while stack and stack[-1] != '(' :
                answer+=stack.pop()
            stack.pop() # ( 버리기

while stack :
    answer+=stack.pop()

print(answer)

