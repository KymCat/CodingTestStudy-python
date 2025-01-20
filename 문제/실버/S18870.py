import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))

uniq_x = sorted(set(x)) # compression X
cp_x_dict = { value:index for index,value in enumerate(uniq_x) }
cp_x = [ cp_x_dict[i] for i in x ]

print(' '.join(map(str, cp_x)))