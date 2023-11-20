n = int(input())
Tree = {}

for i in range(n):
    p, l, r = input().split()
    Tree[p] = [l, r]

def preorder(p):
    if p != '.':
        print(p,end = '')
        preorder(Tree[p][0])
        preorder(Tree[p][1])

def inorder(p):
    if p != '.':
        inorder(Tree[p][0])
        print(p,end ='')
        inorder(Tree[p][1])

def postorder(p):
    if p != '.':
        postorder(Tree[p][0])
        postorder(Tree[p][1])
        print(p,end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')