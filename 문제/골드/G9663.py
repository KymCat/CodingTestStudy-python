import sys

n = int(sys.stdin.readline().rstrip())
queen_location = [-1] * n  # 퀸 위치, 퀸은 한 행에 하나만 놓을 수 있기에 1차원 리스트, idx=행 value=열
def is_move(row, col) : # 같은 열,대각선 위치 판별
    for i in range(row) :
        if queen_location[i] == col or abs(i-row) == abs(queen_location[i] - col) :
            return False
    return True

cnt = 0
def solution(row) :
    global cnt

    if row == n :
        cnt+=1

    else :
        for i in range(n) :
            if is_move(row,i) :
                queen_location[row] = i
                solution(row+1)

solution(0)
print(cnt)