def BFS(x, y):
    global cnt
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = []
    q.append((x, y))
    visited[y][x] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for d in range(4):
            nx, ny = i + dx[d], j+ dy[d]
            if 0<= nx < M and 0 <= ny < N and not visited[ny][nx] and maze[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = visited[j][i] + 1

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)] #1 이동 가능 0 이동할 수 없음
visited = [[0]*M for _ in range(N)]
BFS(0, 0)
print(visited[N-1][M-1])
# print(maze)