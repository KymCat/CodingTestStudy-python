# 중위 순회 : left -> right -> root
# 트리 생성 (2차원 리스트)
n = 7  # 노드 개수
tree = [[] for _ in range(n + 1)]
tree[1] = [2, 3]
tree[2] = [4, 5]
tree[3] = [6, 7]

def postorder(node) :
    if tree[node] :
        postorder(tree[node][0])
        if len(tree[node]) > 1 :
            postorder(tree[node][1])
    print(node, end=" ")

def postorder_stack(root) :
    stack = [root]
    output = []
    while stack :
        node = stack.pop()
        output.append(node)

        if tree[node] :
            stack.append(tree[node][0])
            if len(tree[node]) > 1 :
                stack.append(tree[node][1])

    print(" ".join(map(str, output[::-1])))

postorder(1)
print()
postorder_stack(1)
