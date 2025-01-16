import sys

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

def dfs(network, start) :
    stack = [1]
    visited = set()

    cnt = 0
    while stack :
        com = stack.pop()
        if com not in visited :
            if com != start :
                cnt+=1
            visited.add(com)

            for i in network[com] :
               if i not in visited :
                   stack.append(i)

    return cnt

print(dfs(network, 1))