import sys

input = sys.stdin.readline


T = int(input())
for t in range(T):
    node = int(input())
    tree = [[] for _ in range(node+1)]
    for _ in range(node-1):
        start, end = map(int, input().split())
        tree[end] = start
    a, b = map(int, input().split())
    ap = [a]
    bp = [b]

    while tree[a]:
        ap.append(tree[a])
        a=tree[a]
    while tree[b]:
        bp.append(tree[b])
        b = tree[b]

    deptha = len(ap)-1
    depthb = len(bp) - 1

    while ap[deptha] == bp[depthb]:
        deptha -= 1
        depthb -= 1

    print(ap[deptha+1])