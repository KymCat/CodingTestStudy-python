import sys

l = int(input())
s = list(map(int, sys.stdin.readline().split()))
n = int(input())

if n in s :
    print(0)
else :
    s.append(n)
    s.sort()
    idx = s.index(n)

    start = 1 # n이 리스트중 가장 작은 값이라면 [A,B]에서 A가 1이되어야함..
    if idx != 0 :
        start = s[idx-1] +1
    end = s[idx + 1] - 1

    answer = 0
    for i in range(start,n+1) :
        for j in range(n,end+1) :
            if i == j : continue
            answer+=1
            print(i,j)

    print(answer)