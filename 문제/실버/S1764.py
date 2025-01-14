import sys

# 딕셔너리 보다 set() 더 코드도 간결하고 가독성이 좋음
n,m = map(int, sys.stdin.readline().split())

name = dict()
for _ in range(n) :
    who = sys.stdin.readline().rstrip()
    name[who] = 1

for _ in range(m) :
    who = sys.stdin.readline().rstrip()
    if name.get(who) :
        name[who] += 1
    else :
        name[who] = 1

answer = []
for key, value in name.items() :
    if value == 2 :
        answer.append(key)

print(len(answer))
answer.sort()
for i in answer :
    print(i)
