h,m = map(int, input().split())
# if h == 0 :
#     h = 24
#
# sum = (h*60) + m - 45
# h,m = sum//60, sum%60
# if h == 24 :
#     h = 0
# print(h,m)

if m < 45 :
    if h == 0 :
        h = 23
        m += 60
    else :
        h -= 1
        m+= 60
print(h,m-45)