import sys, math
from collections import defaultdict

n,m = map(int, sys.stdin.readline().split())

info = defaultdict(list)
for _ in range(m) :
    pack, piece = map(int, sys.stdin.readline().split())
    info['pack'].append(pack)
    info['piece'].append(piece)

min_pack = min(info['pack'])
min_piece = min(info['piece'])
print(min(math.ceil(n / 6) * min_pack, (n // 6) * min_pack + (n % 6) * min_piece, min_piece * n))