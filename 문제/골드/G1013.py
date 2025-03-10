import sys, re

t = int(input())
for _ in range(t) :
    case = sys.stdin.readline().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(case)

    if m : print('YES')
    else : print('NO')