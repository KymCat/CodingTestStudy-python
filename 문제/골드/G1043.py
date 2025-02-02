import sys

n, m = map(int, sys.stdin.readline().split()) # 사람 수 / 파티 수
truth = set(sys.stdin.readline().split()[1:]) # 진실을 아는 사람번호 리스트

parties = []
for _ in range(m) :
    parties.append(set(sys.stdin.readline().split()[1:]))

for _ in range(m) :                         # m만큼 반복해서 union() 하는 이유...
    for party in parties :                  # 4가 진실을 알고있고, 4가 4번째 파티에 2를 만났다고 가정하면,
        if party & truth :                  # 2 또한 진실을 알게 되므로 4를 만나기 전 후 파티 모두를 검사해 2를 만난 사람들을 찾아야함.
            truth = truth.union(party)      # 4를 만나기 후는 그대로 for문을 진행하면 되지만 만나기 전은 처음으로 돌아가야함.
                                            # 그런데 이와 같은 상황이 한사람에게만 아닌 모두에게 일어날 수 있으므로 파티수(m)만큼 반복하면서 갱신할 필요있음.
answer = 0
for party in parties :
    if not party & truth :
        answer+=1

print(answer)