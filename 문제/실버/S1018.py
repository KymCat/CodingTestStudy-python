import sys

n,m = map(int, input().split())
board = []
for _ in range(n) :
    board.append(sys.stdin.readline().rstrip())

cnt = []
for i in range(n-7) :
    for j in range(m-7) :
        w_start = 0
        b_start = 0
        for a in range(i,i+8) :
            for b in range(j,j+8) :
                if (a+b) % 2 == 0 :
                    if board[a][b] != 'W':
                        w_start += 1
                    if board[a][b] != 'B' :
                        b_start += 1
                else :
                    if board[a][b] != 'B':
                        w_start += 1
                    if board[a][b] != 'W' :
                        b_start += 1

        cnt.append(min(w_start,b_start))
print(min(cnt))