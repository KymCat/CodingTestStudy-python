import sys
from collections import defaultdict

n = int(input())

tree = defaultdict(list)
for _ in range(n) :
    a,b,c = sys.stdin.readline().split()
    tree[a].append(b)
    tree[a].append(c)

def preorder(node) :
    print(node,end="")
    if tree[node][0] != '.' :
        preorder(tree[node][0])
    if tree[node][1] != '.' :
        preorder(tree[node][1])

def inorder(node) :
    if tree[node][0] != '.' :
        inorder(tree[node][0])

    print(node,end="")
    if tree[node][1] != '.' :
        inorder(tree[node][1])

def postorder(node) :
    if tree[node][0] != '.' :
        postorder(tree[node][0])

    if tree[node][1] != '.' :
        postorder(tree[node][1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')