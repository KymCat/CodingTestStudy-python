import sys

n = int(sys.stdin.readline())
house = []
house.append([0] * (n+1))
for _ in range(n) :
    house.append([0] + list(map(int, sys.stdin.readline().split())))

dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(3)]
# dp[0][r][c] => 가로
# dp[1][r][c] => 세로
# dp[2][r][c] => 대각선

dp[0][1][2] = 1 # (1,2) 시작 좌표 => 가로 배치 : [0][1][2] = 1
for i in range(3,n) : # 시작 좌표와 같은 행은 가로만 가능
    if house[1][i] == 0 :
        dp[0][1][i] += dp[0][1][i-1]

for i in range(2,n+1) :
    for j in range(3,n+1) :
        # (i-1, j-1) ==대각==> (i,j) 오는 방법은 총 3가지...
        # (i-1, j-1)으로 (가로,세로,대각선) 파이프가 도착하여 (i,j)로 가는 방법
        if house[i][j] == 0 and house[i-1][j] == 0 and house[i][j-1] == 0 : # 벽 여부 확인
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1] # 따라서 (i-1, j-1)의 가로,세로,대각선 값들을 더해 주는 것

        if house[i][j] == 0 : # 가로 / 세로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # (i,j-1)으로 (가로,대각선) 파이프가 도착해야 (i,j)로 가로로 올 수 있음
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # (i-1,j)으로 (세로,대각선) 파이프가 도착해야 (i,j)로 세로로 올 수 있음


print(sum(dp[i][n][n] for i in range(3)))
