import sys

while True :
    cnt = 0
    st = sys.stdin.readline().lower().rstrip()
    if st == '#':
        break

    for i in range(len(st)) :
        if st[i] in ['a', 'e', 'i', 'o', 'u'] :
            cnt+=1

    print(cnt)