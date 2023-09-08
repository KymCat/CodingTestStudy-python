import sys

t = int(input())
for _ in range(t) :
    is_vps = sys.stdin.readline().rstrip()
    l, r = 0,0

    for s in is_vps :
        if s == '('  : l+=1
        else : r+=1

        if r>l :
            break

    if r == l :
        print('YES')
    else :
        print('NO')