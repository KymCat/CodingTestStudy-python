import sys

n,m,b = map(int, sys.stdin.readline().split())
map = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = int(1e9)
height = 0

for i in range(257) :
    remove_block = 0
    install_block = 0

    for x in range(n) :
        for y in range(m) :
            if map[x][y] > i :
                remove_block += map[x][y] - i
            else :
                install_block += i - map[x][y]

    # 블럭설치가 더 빠르므로 설치하는 최대수 방향으로..
    if remove_block + b >= install_block :
        if time >= (remove_block*2) + install_block :
            time = (remove_block*2) + install_block
            height = i

print(time, height)
# pypy3 제출