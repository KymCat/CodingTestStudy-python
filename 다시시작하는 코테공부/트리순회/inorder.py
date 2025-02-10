# 중위 순회 : left -> root -> right
# 트리 생성 (2차원 리스트)
n = 7  # 노드 개수
tree = [[] for _ in range(n + 1)]
tree[1] = [2, 3]
tree[2] = [4, 5]
tree[3] = [6, 7]

def inorder(node) :
    if tree[node] :
        inorder(tree[node][0])

    print(node, end=" ")
    if len(tree[node]) > 1 :
        inorder(tree[node][1])

def inorder_stack(root) :
    stack = []
    node = root
    while stack or node :
        while node :
            stack.append(node)
            node = tree[node][0] if tree[node] else None

        node = stack.pop()
        print(node, end=" ")
        node = tree[node][1] if len(tree[node]) > 1 else None

inorder(1)
print()
inorder_stack(1)
