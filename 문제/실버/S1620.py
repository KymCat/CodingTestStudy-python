import sys

n,m = map(int,sys.stdin.readline().split())

pokemon = dict()
number = dict()

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    pokemon[i] = name
    number[name] = i

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(pokemon[int(question)])

    else:
        print(number[question])

# 시간제한 코드 --> 리스트 find에서 많은 시간을 소비하는것 같음
# dic = []
# for _ in range(n) :
#     dic.append(sys.stdin.readline().rstrip())
#
# for _ in range(m) :
#     question = sys.stdin.readline().rstrip()
#     if question.isdigit() :
#         print(dic[int(question)-1])
#
#     else :
#         print(dic.index(question)+1)


