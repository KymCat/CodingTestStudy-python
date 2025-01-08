import sys

m = int(input())

S = set()
for _ in range(m) :
    cal, *num = sys.stdin.readline().split()
    num = int(num[0]) if num else None

    if cal == 'add' :
        S.add(num)

    elif cal == 'remove' :
        if num in S :
            S.remove(num)

    elif cal == 'check' :
        if num in S : print('1')
        else : print('0')

    elif cal == 'toggle' :
        if num in S :
            S.remove(num)
        else :
            S.add(num)

    elif cal == 'all' :
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

    else :
        S = set()
