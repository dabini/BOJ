import sys

def BFS(x, y):
    global answer
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = set([(x,y,arr[y][x])])

    while q:
        i, j, ans = q.pop()
        for d in range(4):
            nx, ny = i+dx[d], j+dy[d]
            if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] not in ans:
                q.add((nx, ny, ans+arr[ny][nx]))
                answer = max(answer, len(ans)+1)

input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
answer = 1

BFS(0, 0)
print(answer)