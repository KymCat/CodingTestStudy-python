while True :
    s = list(map(int, input()))
    if s[0] == 0 :
        break

    elif s == list(reversed(s)) :
        print('yes')
    else :
        print('no')


