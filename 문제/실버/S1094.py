x = int(input())
stick = [64,32,16,8,4,2,1,1]

cnt = 0
for i in stick :
    if x == 0 :
        break
    else :
        if x < i:
            continue
        else :
            x -= i
            cnt +=1

print(cnt)