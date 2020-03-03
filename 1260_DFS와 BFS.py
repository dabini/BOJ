def DFS(V):
    global visited
    visited.append(V)
    for i in range(N+1):
        if field[V][i] == 1 and i not in visited:
            visited = DFS(i)
    return visited

def BFS(V):
    q = [V]
    res = [V]
    while q:
        now = q.pop(0)
        for new in range(N+1):
            if field[now][new] == 1 and new not in res:
                res.append(new)
                q.append(new)
    return res


N, M, V = map(int, input().split())
field = [[0] * (N+1) for _ in range(N+1)]
visited = []
for m in range(M):
     a, b = map(int, input().split())
     field[a][b] = 1
     field[b][a] = 1
DFS(V)
print(*visited)
print(*BFS(V))