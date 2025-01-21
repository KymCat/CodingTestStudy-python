import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

i = 0
cnt = 0 # 답
length = 0 # IOI 패턴 반복횟수
while i < m-1 :
    if s[i:i+3] == 'IOI' :
        length+=1
        if length >= n : # N=2 이고 S = IOIOIOI 일때, length >= n 이어야 연속된 IOIOI를 카운팅가능
            cnt+=1
        i+=2

    else :
        i+=1
        length = 0

print(cnt)