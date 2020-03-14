def DFS(a):
    res.add(a)
    stack.append(a)
    now = stack[-1]
    visited.append(a)
    for new in range(num+1):
        if arr[now][new] and new not in visited:
            DFS(new)
            stack.pop()
            visited.remove(new)
    return res
num = int(input())
arr = [[0]*(num+1) for _ in range(num+1)]
stack = []
visited = []
res = set()
for _ in range(int(input())):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1
DFS(1)
print(len(res)-1)