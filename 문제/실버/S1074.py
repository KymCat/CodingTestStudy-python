import sys

def dnc(x,y,n) : # x,y는 시작 좌표, n은 한변의 길이
    global cnt
    if x>r or x+n <=r or y>c or y+n <=c : # (r,c) 가 범위내에 포함되지 않으면 전체횟수 반환
        cnt+=n**2
        return

    if n > 2 :
        n//=2
        dnc(x, y, n)
        dnc(x, y+n, n)
        dnc(x+n, y, n)
        dnc(x+n, y+n, n)
    else :
        if x==r and y==c :
            print(cnt)
        elif x==r and y+1 == c :
            print(cnt+1)
        elif x+1 == r and y==c :
            print(cnt+2)
        else :
            print(cnt+3)
        sys.exit()


n,r,c = map(int, sys.stdin.readline().split())
cnt = 0
dnc(0,0,2**n)