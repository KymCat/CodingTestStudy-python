import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))

cm = set(A) & set(B)
ans = []
while cm :
    later = max(cm)
    ans.append(later)

    idx_A = A.index(later)
    idx_B = B.index(later)

    A = A[idx_A+1:]
    B = B[idx_B+1:]
    cm = set(A) & set(B)

print(len(ans))
print(*ans)