import sys
def preorder_traverse(T):
    if T:
        print("%d" %T, end=' ')
        preorder_traverse(tree[T][1])
        preorder_traverse(tree[T][2])


input = sys.stdin.readline
N = int(input())
tree = [[0]*2 for _ in range(N)]
for n in range(N):
    root, left, right = map(str, input().split())
    if left != '.':
        tree[n][0] =ord(left) - ord('A')
    if right != '.':
        tree[n][1] = ord(right) - ord('A')
print(tree)
# preorder_traverse(0)