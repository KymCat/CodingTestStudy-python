import math
n = int(input())

cnt = 0
for i in reversed(str(math.factorial(n))) :
    if i != '0' :
        break
    else :
        cnt+=1

print(cnt)
