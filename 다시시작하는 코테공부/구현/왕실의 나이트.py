import sys
ch = sys.stdin.readline()
ch_n = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x,y = ch_n[ch[0]], int(ch[1])

# 좌표이동경우 (+1 +2) (+1 -2) (-1 +2) (-1 -2) (+2,+1) (+2,-1) (-2,+1) (-2,-1)
dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

count = 0
for i in range(len(dx)) :
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
        continue
    count+=1

print(count)


# 아래는 해설
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # +1을 좌표가 (1,1) 부터니까
# ord() -- > 문자를 아스키코드에 속한 정수로 바꾸어주는 함수

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps :
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :
        result+=1

print(result)