# 전위 순회 : root -> left -> right
# 트리 생성 (2차원 리스트)
n = 7  # 노드 개수
tree = [[] for _ in range(n + 1)]
tree[1] = [2, 3]
tree[2] = [4, 5]
tree[3] = [6, 7]

# 재귀
def preorder(node) :
    print(node, end=" ")
    if tree[node] :
        preorder(tree[node][0])
        if len(tree[node]) > 1 :
            preorder(tree[node][1])

def preorder_stack(root) :
    stack = [root]
    while stack :
        node = stack.pop()
        print(node, end=" ")

        if tree[node] :
            if len(tree[node]) > 1 :
                stack.append(tree[node][1]) # stack은 LIFO 구조이기에 오른쪽부터 넣어야함
            stack.append(tree[node][0])


preorder(1)
print()
preorder_stack(1)