import sys

expr = sys.stdin.readline().rstrip()
expr_split = expr.split('-')

for i in range(len(expr_split)) :
    if '+' in expr_split[i] :
        tmp = list(map(int,expr_split[i].split('+')))
        expr_split[i] = sum(tmp)

sub = int(expr_split[0])
for i in range(1,len(expr_split)) :
    sub -= int(expr_split[i])

print(sub)


