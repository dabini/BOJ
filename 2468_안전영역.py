import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(i, j, num):
    global visited
    q = [(i, j)]
    visited[j][i] = num
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<= nx < N and 0 <= ny < N and arr[ny][nx] > num and visited[ny][nx] < num:
                q.append((nx, ny))
                visited[ny][nx] = num

N = int(input())
max_num = -1
arr = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if max_num < arr[y][x]:
            max_num = arr[y][x]

max_cnt = 1
num = 1

visited = [[0]*N for _ in range(N)]
while num <= max_num:
    cnt = 0
    for j in range(N):
        for i in range(N):
            if arr[j][i] > num and visited[j][i] < num:
                BFS(i, j, num)
                cnt += 1
    if cnt == 0:
        break
    if cnt > max_cnt:
        max_cnt = cnt
    num += 1

print(max_cnt)