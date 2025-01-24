import sys

t = int(input())

triangle = [0] * 101
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
triangle[4] = 2
triangle[5] = 2

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())

    for i in range(6,n+1) :
        triangle[i] = triangle[i-1] + (triangle[i-5])
    print(triangle[n])