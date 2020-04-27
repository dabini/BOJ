import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node):
    children = tree[node]
    for c in children:
        if not visited[c]:
            parent[c] = node
            visited[c] = True
            dfs(c)

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited[1] = 1
dfs(1)
for i in range(2, N+1):
    print(parent[i])
