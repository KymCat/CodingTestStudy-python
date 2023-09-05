import sys

t = int(input())
for _ in range(t) :
    ox = sys.stdin.readline().rstrip()
    score = 0
    stream = 0 # 연속점수
    for i in ox :
        if i == 'O' :
            stream += 1
            score += stream
        else :
            stream = 0
    print(score)