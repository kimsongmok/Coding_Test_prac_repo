import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(preorder):
    if not preorder:
        return None

    root = Node(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        if value < stack[-1].data:
            stack[-1].left = Node(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].data < value:
                last = stack.pop()
            last.right = Node(value)
            stack.append(last.right)

    return root

def iterative_postorder(root):
    if not root:
        return []

    stack, postorder = [], []
    node = root
    last_node_visited = None

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_node_visited != peek_node.right:
                node = peek_node.right
            else:
                postorder.append(peek_node.data)
                last_node_visited = stack.pop()

    return postorder

# 입력 받기
preorder_input = [int(line.strip()) for line in sys.stdin if line.strip()]

# 트리 구축
root = build_tree(preorder_input)

# 후위 순회 결과 계산
postorder_result = iterative_postorder(root)

# 결과 출력
for num in postorder_result:
    print(num)
