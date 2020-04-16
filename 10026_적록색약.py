import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, col):
    visited[y][x] = 1
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == col and not visited[ny][nx]:
            DFS(nx, ny, col)

def DFS2(x, y, col):
    visited2[y][x] = 1
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if col == "B":
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == "B" and not visited2[ny][nx]:
                DFS2(nx, ny, arr[ny][nx])
        else:
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] != 'B' and not visited2[ny][nx]:
                DFS2(nx, ny, arr[ny][nx])

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
# print(arr)
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
cnt = 0
cnt2 = 0

for j in range(N):
    for i in range(N):
        if arr[j][i] == 'R' and not visited[j][i]:
            DFS(i, j, 'R')
            cnt += 1
        elif arr[j][i] == 'G' and not visited[j][i]:
            DFS(i, j, 'G')
            cnt += 1
        elif arr[j][i] == 'B' and not visited[j][i]:
            DFS(i, j, 'B')
            cnt += 1

for y in range(N):
    for x in range(N):
        if arr[y][x] != 'B' and not visited2[y][x]:
            DFS2(x, y, arr[y][x])
            cnt2 += 1
        elif arr[y][x] == 'B' and not visited2[y][x]:
            DFS2(x, y, arr[y][x])
            cnt2 += 1
print(cnt)
print(cnt2)