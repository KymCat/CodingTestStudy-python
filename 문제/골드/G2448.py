import sys

n = int(sys.stdin.readline().rstrip())

arr = [[' ' for _ in range(2*n-1)] for _ in range(n)]

def draw(n, x, y, arr) :
    if n == 3 :
        arr[x][y] = '*'
        arr[x+1][y-1] = '*'
        arr[x+1][y+1] = '*'
        for i in range(-2,3) :
            arr[x+2][y+i] = '*'
        return

    half = n//2
    draw(half, x, y, arr)
    draw(half, x+half, y-half, arr)
    draw(half, x+half, y+half, arr)

draw(n,0,n-1,arr)
for i in arr :
    print("".join(i))
