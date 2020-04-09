from itertools import combinations
import copy
"""
조합으로 벽 세울 수 있는 3가지 경우 만들기
각 경우마다 BFS 돌려보고 안전영역 최대크기 구하기
카피하기..?
"""
def BFS(v):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q.append((v[0], v[1]))
    visited[v[1]][v[0]] = 2

    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx, ny = x + dx[d] , y +dy[d]
            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = 2

N, M = map(int, input().split()) #세로 가로
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
v_lst = []
for n in range(N):
    for m in range(M):
        if arr[n][m] == 0:
            lst.append((m, n))
        elif arr[n][m] == 2:
            v_lst.append((m, n))

p_lst = list(combinations(lst, 3))
# print(p_lst)

q = []
res = -1
for p in p_lst:
    cnt = 0
    arr[p[0][1]][p[0][0]] = arr[p[1][1]][p[1][0]] = arr[p[2][1]][p[2][0]] = 1
    visited = copy.deepcopy(arr)
    for v in v_lst:
        BFS(v)

    for j in range(N):
        for i in range(M):
           if visited[j][i] == 0:
               cnt += 1
    if cnt > res:
        res = cnt
    arr[p[0][1]][p[0][0]] = arr[p[1][1]][p[1][0]] = arr[p[2][1]][p[2][0]] = 0

print(res)