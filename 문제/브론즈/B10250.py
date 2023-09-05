t = int(input())

for _ in range(t) :
    h,w,n = map(int,input().split())
    # floor = n - h*(n//h)
    floor = n % h
    if floor == 0 :
        floor = h

    room = n//h
    if n%h != 0 :
        room +=1

    # print(str(floor) + str(room).zfill(2))
    print(f'{floor*100 + room}')

