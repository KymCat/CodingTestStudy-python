import sys
from collections import deque

n = int(input())
for _ in range(n) :
    order = sys.stdin.readline().rstrip()

    length = int(input())
    if length > 0 :
        array = deque(map(int,sys.stdin.readline().rstrip().strip('[]').split(',')))
    else :
        array = deque(sys.stdin.readline().rstrip().strip('[]'))

    error_code = 0
    cnt = 0
    for i in order :
        if i == 'R' :
            cnt+=1
        else :
            try :
                if cnt%2 == 0 :
                    array.popleft()
                else :
                    array.pop()

            except :
                print('error')
                error_code = 1
                break

    if not error_code :
        if cnt%2 != 0 :
            array.reverse()
        print('[' + ','.join(map(str,array)) + ']')
        # print(str(array).replace(' ',''))