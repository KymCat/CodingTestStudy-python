'''
input
3
BBW
WBB
WBW

output
2
'''

n = int(input())
board = [ list(input().rstrip()) for _ in range(n) ]

# 원래 입력과 완전 반대되는 판만들기
board_r = [ stone[:] for stone in board ]
for i in range(n) :
    for j in range(n) :
        if board_r[i][j] == 'B' :
            board_r[i][j] = 'W'
        else : board_r[i][j] = 'B'

answer = n*n
# 1<<n == 2**n (N개 행이 뒤집힐 수 있는 모든 경우의 수)
for case in range(1<<n) :
    tmp = []
    for i in range(n) :
        if case & (1<<i) :
            tmp.append(board_r[i])
        else : tmp.append(board[i])

    count = 0
    for i in range(n) :
        col_count = 0
        for j in range(n) :
            if tmp[j][i] == 'W' :
                col_count += 1

        # 열도 한번 뒤집는 것 까지 고려해서..
        count += min(col_count, n - col_count)
    answer = min(count, answer)

print(answer)