n = int(input())
if n <= 99 :
    print(n)

else :

    cnt = 99
    for i in range(111, n+1) :
        h = i//100
        t = (i%100)//10
        o = i%10

        if t-h == o-t :
            cnt+=1

    print(cnt)
