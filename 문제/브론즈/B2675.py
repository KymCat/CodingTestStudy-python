t = int(input())
for _ in range(t) :
    n,s = map(str, input().split())
    for i in range(len(s)) :
        print(s[i]*int(n), end="")
    print()