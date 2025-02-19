import sys

n = int(input())
switch = list(map(int,sys.stdin.readline().split()))
m = int(input())
for _ in range(m) :
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1 :
        k = n//num
        for i in range(1,k+1) :
            if switch[i*num-1] :
                switch[i*num-1] -= 1
            else : switch[i*num-1] +=1

    else :
        i = 1
        while 0 <= (num-1)-i and (num-1)+i < n :
            if switch[(num-1)-i] == switch[(num-1)+i] :
                i+=1
            else : break

        i-=1
        for j in range((num-1)-i, (num-1)+i+1) :
            if switch[j] :
                switch[j] -= 1
            else : switch[j] += 1

for i in range(len(switch)) :
    if i != 0 and i%20 == 0 :
        print()
    print(switch[i],end=" ")