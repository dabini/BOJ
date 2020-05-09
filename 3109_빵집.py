import sys
input = sys.stdin.readline

dx = [-1, 0,  1]

def DFS(r, c):
    global res
    if c == C-1:
        return True
    for d in range(3):
        nr = r + dx[d]
        if 0<= nr < R and map[nr][c + 1] == "." and not visited[nr][c + 1]:
            visited[nr][c + 1] = 1
            if DFS(nr, c + 1):
                return True
    return False


R, C = map(int, input().split())
map = list(input().strip() for _ in range(R))
visited = [[0]*C for _ in range(R)]
# print(map)
res = 0

for r in range(R):
    if map[r][0] == ".":
        if DFS(r, 0):
            res += 1
print(res)
