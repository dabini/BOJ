import sys

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())