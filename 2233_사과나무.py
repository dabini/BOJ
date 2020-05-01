import sys

def DFS(tree):
    stack = [0]
    n = 1
    for t in tree:
        if t == '0':
            stack.append(n)
            lst.append(n)
            n += 1
        else:
            k = stack.pop()
            lst.append(k)
            parents[k] = stack[-1]

input = sys.stdin.readline

N = int(input())
tree = input().strip()
X, Y = map(int, input().split())
lst = [0]
parents = [0 for _ in range(N+1)]
DFS(tree)
# print(lst)
# print(parents)

X_parents = [lst[X]]
Y_parents = [lst[Y]]

while parents[lst[X]]:
    X_parents.append(parents[lst[X]])
    lst[X] = parents[lst[X]]
while parents[lst[Y]]:
    Y_parents.append(parents[lst[Y]])
    lst[Y] = parents[lst[Y]]

dx = len(X_parents) - 1
dy = len(Y_parents) - 1

while X_parents[dx] == Y_parents[dy]:
    dx -= 1
    dy -= 1

idx = X_parents[dx+1]
for i in range(len((lst))):
    if idx == lst[i]:
        print(i, end=" ")