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

def BFS(x, y):
    global res
    q = [(x, y)]
    


Y, X = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(Y)]
# print(ice)
res = 0
while True:
    ice_check = [[0] * X for __ in range(Y)]
    check = True
    for y in range(Y):
        for x in range(X):
            if ice[y][x] != 0:
                j, i = y, x
                check = False
                DFS(i, j)

    for j in range(Y):
        for i in range(X):
            if ice[j][i] != 0:
                y, x = j, i
                BFS(x, y)
    if check:
        res = 0
        break
    else:
        ice = ice_check
        res += 1
print(res)