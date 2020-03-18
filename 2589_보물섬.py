# def BFS(x, y):
#     global cnt, res, visited
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     q = [(x, y)]
#     res = [(x, y)]
#     visited = [(x, y)]
#     while q:
#         (i, j) = q.pop(0)
#         for d in range(4):
#             newy = j + dy[d]
#             newx = i + dx[d]
#             if 0 <= newx < X and 0<= newy < Y:
#                 if mymap[newy][newx] == "L" and (newx, newy) not in res:
#                     q.append((newx, newy))
#                     res.append((newx, newy))
#                     visited.append((newx, newy))
#                     cnt += 1
#     return cnt
#
# Y, X = map(int, input().split())
# mymap = [list(input()) for _ in range(Y)]
# ans = 98765432
# visited = []
# for y in range(Y):
#     for x in range(X):
#         if mymap[y][x] == 'L' and (x, y) not in visited:
#             res = []
#             cnt = 0
#             BFS(x, y)
#             if ans > cnt:
#                 ans = cnt
# print(ans)

from collections import deque

def bfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((x,y,0))
    visited[y][x] = 1
    cnt = 0
    while q:
        i, j, tmp = q.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < shark_x and 0 <= ny < Y:
                if visited[ny][nx] == 0 and mymap[ny][nx] == "L":
                    q.append((nx, ny, tmp+1))
                    visited[ny][nx] = 1
                    if cnt < tmp+1:
                        cnt = tmp+1
    return cnt

Y, shark_x = map(int, input().split())
mymap = [list(input()) for _ in range(Y)]
visited = [[0] * shark_x for _ in range(Y)]
res = 0

for y in range(Y):
    for x in range(shark_x):
        if mymap[y][x] == 'L':
            visited = [[0] * shark_x for _ in range(Y)] #값을 돌릴 때 마다 초기화 시켜주기
            res = max(res, bfs(x, y))
print(res)
