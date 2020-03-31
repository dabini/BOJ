import sys
sys.setrecursionlimit(10**8)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, n):
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 < arr[nx][ny] and visited[nx][ny] <n:
            visited[nx][ny] = n
            dfs(nx, ny, n)
        elif arr[x][y] > 0 and not arr[nx][ny] and visited[nx][ny] < n:
            arr[x][y] -= 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def solve():
    n = 1
    check = True
    while check:
        check = False
        for x in range(1, N-1):
            for y in range(1, M-1):
                if arr[x][y] and visited[x][y] <n:
                    if not check:
                        visited[x][y] = n
                        dfs(x, y, n)
                        check = True
                    else:
                        return n-1
        n += 1
    return 0

print(solve())


#bfs
# import sys
#
# def bfs(y, x):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     queue = [(x, y)]
#     vis[y][x] = True
#
#     while queue:
#         x, y = queue.pop(0)
#         for i in range(4):
#             xi = x + dx[i]
#             yi = y + dy[i]
#             if 0 <= xi < M and 0 <= yi < N and not vis[yi][xi]:
#                 if arctic[yi][xi] == 0 and arctic[y][x] > 0:
#                     arctic[y][x] -= 1
#                 elif arctic[yi][xi] >= 1:
#                     vis[yi][xi] = True
#                     queue.append((xi, yi))
#     return 1
#
#
# N, M = map(int, sys.stdin.readline().split())
# arctic = []
# for i in range(N):
#     arctic.append(list(map(int, sys.stdin.readline().split())))
#
# cnt = 0
# time = -1
# while cnt < 2:
#     vis = [[False] * M for i in range(N)]
#     cnt = 0
#     is_fin = True
#     for j in range(N):
#         for i in range(M):
#             if arctic[j][i] > 0 and not vis[j][i]:
#                 is_fin = False
#                 cnt += bfs(j, i)
#
#     time += 1
#     if is_fin:
#         time = 0
#         break
#
# print(time)