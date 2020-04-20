"""
한 번에 한 방향에서 벽까지 이동 / 방향 바꿀 때마다 최소이동횟수 +1 하기
R이 B보다 O에 먼저 들어가야 성공! 이동횟수 출력
만약 R이 10번 이내로 O에 들어가지 못하거나 B가 먼저 들어갈 경우 -1 출력
#벽 . 이동가능한 통로?
필요한거.. q, visited,
"""
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def move(x, y, dx, dy):
    cnt = 0
    #다음이 벽이 거나 현재가 구멍일 때까지만
    while game[y+dy][x+dx] != "#" and game[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def BFS():
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            break
        for d in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[d], dy[d])
            nbx, nby, bcnt = move(bx, by, dx[d], dy[d] )
            if game[nby][nbx] != 'O':
                if game[nry][nrx] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[d]
                        nry -= dy[d]
                    else:
                        nbx -= dx[d]
                        nby -= dy[d]
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append((nrx, nry, nbx, nby, depth+1))
    print(-1)


input = sys.stdin.readline
N, M = map(int, input().split())
game = [list(input().strip()) for _ in range(N)]
q = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for j in range(N):
    for i in range(M):
        if game[j][i] == 'R':
            ry, rx = j , i
        elif game[j][i] == "B":
            by, bx = j,  i
q.append((rx, ry, bx, by, 1))
visited[ry][rx][by][bx] = True

BFS()
