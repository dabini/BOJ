import sys
input = sys.stdin.readline

def preorder_traverse(T):
    if T:
        # res.add(T)
        print(chr(T + ord('A')-1), end='')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][0])
        print(chr(T + ord('A')-1), end='')
        inorder_traverse(tree[T][1])

def outorder_traverse(T):
    if T:
        outorder_traverse(tree[T][0])
        outorder_traverse(tree[T][1])
        print(chr(T + ord('A')-1), end='')


input = sys.stdin.readline
N = int(input())
tree = [[0]*2 for _ in range(N+1)]
for n in range(1, N+1):
    root, left, right = map(str, input().split())
    if left != '.':
        tree[ord(root) - ord('A') + 1][0] =ord(left) - ord('A') + 1
    if right != '.':
        tree[ord(root) - ord('A') + 1][1] = ord(right) - ord('A') + 1
# print(tree)
preorder_traverse(1)
print()
inorder_traverse(1)
print()
outorder_traverse(1)