def BFS(x, y):
    global cnt
    q.append((x, y))
    visited[y][x] = 1
    cnt += 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        i, j = q.pop(0)
        for d in range(4):
            nx, ny = i+dx[d], j+dy[d]
            if 0<=nx<N and 0<=ny<M and arr[ny][nx] == 0 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = 1
                cnt += 1
    res.append(cnt)



M, N, K = map(int, input().split())
arr = [[0]*(N) for _ in range(M)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            arr[j][i] = 1

visited = [[0]*(N) for _ in range(M)]
res = []
q = []
for y in range(M):
    for x in range(N):
        if arr[y][x] == 0 and not visited[y][x]:
            cnt = 0
            BFS(x, y)
# print(arr)
print(len(res))
print(*sorted(res))