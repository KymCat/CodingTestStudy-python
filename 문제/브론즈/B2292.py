n = int(input())

start = n-1
if start == 0 :
    print(1)

for i in range(1,n) :

    start -= 6 * i
    if start <= 0 :
        print(i+1)
        break