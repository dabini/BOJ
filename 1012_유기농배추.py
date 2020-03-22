def find(x, y):
    arr[y][x] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for d in range(4):
        nx, ny = x+dx[d], y +dy[d]
        if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 1:
            find(nx, ny)

T = int(input())
for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1


        for n in range(N):
            for m in range(M):
                if arr[n][m] == 1:
                    find(m, n)
                    cnt += 1
    print(cnt)