def DFS(x, y):
    global cnt
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0  #빙산 주변 0의 개수 체크
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < Y and 0 <= nx < X:
            if ice[ny][nx] == 0:
                cnt +=1
        if ice[y][x] - cnt < 0:
            ice_check[y][x]  = 0
        else:
            ice_check[y][x] = ice[y][x] - cnt

def BFS(x, y): #빙하가 두 조각으로 나뉘는 지를 비교)
    global max_len
    visited[y][x] += 1
    q.append((y, x))
    lst.append((y, x))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        y, x = q.pop(0)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < Y and 0 <= nx < X:
                if ice[ny][nx] and not visited[ny][nx]:
                    q.append((ny, nx))
                    lst.append((ny, nx))
                    visited[ny][nx] += 1
    if max_len < len(lst):
        max_len = len(lst)


Y, X = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(Y)]
# print(ice)
res = 0
num = 0
while True:
    ice_check = [[0] * X for __ in range(Y)]

    q = []
    max_len = 0
    visited = [[0] * X for __ in range(Y)]
    for j in range(Y):
        for i in range(X):
            if ice[j][i] != 0:
                y, x = j, i
                lst = []
                BFS(x, y)
                num += 1
    res += 1

    check = True
    for y in range(Y):
        for x in range(X):
            if ice[y][x] != 0:
                j, i = y, x
                check = False
                DFS(i, j)
    ice = ice_check


    if num != max_len:
        break

    elif check:
        res = 0
        break

print(res)