M, N = map(int, input().split())
chess = [list(map(str, input())) for _ in range(M)]
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for y in range(M):
    for x in range(N):
        check = chess[y][x]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<= ny < M and 0<= nx < N and chess[ny][nx] == check:
                if check == "B":
                    chess[ny][nx] = 'W'
                    cnt += 1
                elif check == "W":
                    chess[ny][nx] = 'B'
                    cnt += 1
print(cnt)