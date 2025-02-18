import sys
from collections import defaultdict

n,score,p = map(int,sys.stdin.readline().split())
ranking = []
if n :
    ranking = list(map(int,sys.stdin.readline().split()))

if score in ranking and ranking[-1] == score and len(ranking) == p :
    print(-1)

else :
    ranking.append(score)
    ranking.sort(reverse=True)

    ranking_dict = defaultdict(int)
    for idx, value in enumerate(ranking) :
        if not ranking_dict[value] :
            ranking_dict[value] = idx+1
            continue

        idx+=1

    if ranking_dict[score] > p :
        print(-1)
    else :
        print(ranking_dict[score])