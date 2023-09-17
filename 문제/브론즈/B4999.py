import sys
j = sys.stdin.readline().rstrip()
d = sys.stdin.readline().rstrip()

print( 'go' if len(j) >= len(d) else 'no')