import sys

def round2(num) :
    return int(num) + (1 if num-int(num) >= 0.5 else 0)

n = int(input())
if n == 0 :
    print(0)

else :
    rank = []
    for _ in range(n) :
        rank.append(int(sys.stdin.readline()))

    trim = round2(n * 0.15)
    trim_rank = sorted(rank)[trim: n-trim]
    print(round2(sum(trim_rank)/(len(trim_rank))))