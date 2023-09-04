n = int(input())
m = int(input())

start = n - n%100
for i in range(0,100) :
    if (start + i)%m == 0 :
        print(str(i).zfill(2))
        break

# str()[-2:] 방법도 있음