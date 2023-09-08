import sys

n = int(input())

result = []
for _ in range(n) :
    age, name = sys.stdin.readline().rstrip().split()
    result.append((int(age), name))

for a,n in sorted(result, key= lambda x:x[0]) :
    print(a,n)