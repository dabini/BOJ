# import sys
# from collections import deque
# input = sys.stdin.readline
# def bfs():
#     visited = [[False]*1001 for _ in range(1001)]
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     q = deque()
#     for y in range(h):
#         for x in range(w):
#             if building[y][x] == '*':
#                 q.append((x, y, 1))
#                 visited[y][x] = 0
#     while q:
#         x, y, cnt = q.popleft()
#         for d in range(4):
#             nx, ny = x+dx[d], y+dy[d]
#             if nx < 0 or nx >=w or ny <0 or ny >=h:
#                 continue
#             if building[ny][nx] == "." and visited[ny][nx] > cnt:
#                 visited[ny][nx] = cnt
#                 q.append((nx, ny, cnt+1))
#
#     for j in range(h):
#         for i in range(w):
#             if building[j][i] == "@":
#                 q.append((i, j, 1))
#
#     while q:
#         x, y, cnt = q.popleft()
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if nx < 0 or nx >=w or ny <0 or ny >=h:
#                 print(cnt)
#                 return
#             if building[ny][nx] == "." and visited[ny][nx] > cnt:
#                 visited[ny][nx] = -1
#                 q.append((nx, ny, cnt + 1))
#
#     print('IMPOSSIBLE')
#
# for t in range(int(input())):
#     w, h = map(int, input().split())
#     building = []
#     for _ in range(h):
#         building.append(input())
#     bfs()

# from collections import deque
# import sys
#
# r = sys.stdin.readline
#
#
# def bfs():
#     q = deque()
#     xx = (0, 0, 1, -1)  # 상,하,좌,우
#     yy = (1, -1, 0, 0)
#     visit = [[float('inf')] * 1001 for i in range(1001)]
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '*':  # 불이면
#                 q.append((i, j, 1))  # 큐에 삽입
#                 visit[i][j] = 0
#     while q:
#         x, y, cnt = q.popleft()
#         for i in range(4):
#             X = x + xx[i]
#             Y = y + yy[i]
#             if X < 0 or X >= h or Y < 0 or Y >= w:
#                 continue
#             if arr[X][Y] == '.' and visit[X][Y] > cnt:
#                 visit[X][Y] = cnt  # 불이 도달하는 시간을 저장
#                 q.append((X, Y, cnt + 1))
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '@':  # 상근이
#                 q.append((i, j, 1))  # 큐에 삽입
#     while q:
#         x, y, cnt = q.popleft()
#         for i in range(4):
#             X = x + xx[i]
#             Y = y + yy[i]
#             if X < 0 or X >= h or Y < 0 or Y >= w:  # 탈출했다면
#                 print(cnt)
#                 return
#             if arr[X][Y] == '.' and visit[X][Y] > cnt:  # 빈 공간이고, 불이 옮겨붙지 않았다면
#                 visit[X][Y] = -1
#                 q.append((X, Y, cnt + 1))
#
#     print('IMPOSSIBLE')  # 탈출할 수 없다면
#
#
# for z in range(int(r())):
#     arr = []
#     w, h = map(int, r().split())
#     for i in range(h):
#         arr.append(r())
#     bfs()

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((sx, sy, 0))
    visited[sx][sy] = 1
    while q:
        x, y, cnt = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                if cnt == 1:
                    continue
                print(visited[x][y])
                return
            if visited[nx][ny] or building[nx][ny] == '#':
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny, cnt))
    print("IMPOSSIBLE")

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    q = deque()
    sx, sy = 0, 0

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                q.append((i, j, 1))
                visited[i][j] = 1
            elif building[i][j] == '@':
                sx, sy = i, j
                building[i][j] = '.'
            else:
                visited[i][j] = 0
    bfs()
