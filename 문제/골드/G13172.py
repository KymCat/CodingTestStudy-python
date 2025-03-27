import sys, math

m = int(sys.stdin.readline())

X = 1_000_000_007
answer = 0

dice = []
for _ in range(m) :
    n,s = map(int, sys.stdin.readline().split())
    a = s // math.gcd(n,s)
    b = n // math.gcd(n,s)

    b_inverse = pow(b, X-2, X)
    answer += (a * b_inverse) % X
    answer %= X

print(answer)
