import sys

n = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
t,p = map(int, sys.stdin.readline().split())

size_answer = 6
for i in size :
    if i == 0 : size_answer -=1
    elif i <= t : continue
    elif i%t == 0 : # t가 5, i가 10일때 묶음은 2묶음만 필요하므로
        size_answer += i//t - 1
        continue

    size_answer += i // t

print(size_answer)
print(n//p, n%p)