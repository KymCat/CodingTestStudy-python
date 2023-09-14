import sys
n = int(input())

crd = []
for _ in range(n) :
    x,y= map(int,sys.stdin.readline().split())
    crd.append((y,x))

crd.sort()
for y,x in crd :
    print(x,y)