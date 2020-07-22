def DFS(st):
    visited.append(st)
    for now in range(1, N+1):
        if arr[st][now] and now not in visited:
            DFS(now)

def BFS(st):
    q = [st]
    res = [st]
    while q:
        now = q.pop(0)
        for new in range(N+1):
            if arr[now][new] and new not in res:
                res.append(new)
                q.append(new)
    return res

N, V, num = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = []
for _ in range(V):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

# print(arr)
DFS(num)
print(*visited)
print(*BFS(num))

