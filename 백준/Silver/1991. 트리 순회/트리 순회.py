import sys

input = lambda: sys.stdin.readline().rstrip()

class Node(object):
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right
        
def preorder(node, tree):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left], tree)
    if node.right != '.':
        preorder(tree[node.right], tree)
        
def inorder(node, tree):
    if node.left != '.':
        inorder(tree[node.left], tree)
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right], tree)
    
def postorder(node, tree):
    if node.left != '.':
        postorder(tree[node.left], tree)
    if node.right != '.':
        postorder(tree[node.right], tree)
    print(node.item, end='')
    
n = int(input())
tree = {}
for _ in range(n):
    i, l, f = input().split()
    tree[i] = Node(i, l, f)
preorder(tree['A'], tree)
print()
inorder(tree['A'], tree)
print()
postorder(tree['A'], tree)