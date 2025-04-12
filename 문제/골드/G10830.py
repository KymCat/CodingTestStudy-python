import sys

n,b = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n) :
    arr.append(list(map(int,sys.stdin.readline().split())))

def mul(arr1, arr2) :
    result = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            result[i][j] = (sum(arr1[i][k] * arr2[k][j] for k in range(n))) % 1000

    return result
def power(arr, b) :
    if b == 1 :
        return arr

    if b % 2 == 0 :
        half = power(arr, b//2)
        return mul(half, half)

    else :
        return mul(arr, power(arr, b-1))

ans = power(arr,b)
for i in range(n) :
    for j in range(n) :
        print(ans[i][j] % 1000 , end=" ")
    print()