n = int(input())
score = list(map(int, input().split()))
m = score.pop(score.index(max(score)))

result = 0
for i in score :
    result = result + (i/m*100)

print((result + 100)/n)