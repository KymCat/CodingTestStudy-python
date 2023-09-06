import sys

def solution() :
    n, *num = map(int, sys.stdin.buffer.read().splitlines())
    stack = []
    result = []
    push_data = 1

    for i in num :
        while push_data <= i :
            stack.append(push_data)
            result.append('+')
            push_data += 1

        if stack.pop() != i :
            return 'NO'
        else :
            result.append('-')

    return '\n'.join(result)

print(solution())

# n = int(input())
#
# stack = []
# result = []
# push_data = 1
#
# is_no = False
# for _ in range(n) :
#     num = int(input())
#
#     while push_data <= num :
#         stack.append(push_data)
#         result.append('+')
#         push_data += 1
#
#     if stack[-1] == num :
#         stack.pop()
#         result.append('-')
#     else :
#         is_no = True
#         break
#
# if is_no :
#     print('NO')
# else :
#     for i in result :
#         print(i)