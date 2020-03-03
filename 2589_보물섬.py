def BFS(x, y):
    global cnt, res, visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = [(x, y)]
    res = [(x, y)]
    visited = [(x, y)]
    while q:
        (i, j) = q.pop(0)
        for d in range(4):
            newy = j + dy[d]
            newx = i + dx[d]
            if 0 <= newx < X and 0<= newy < Y:
                if mymap[newy][newx] == "L" and (newx, newy) not in res:
                    q.append((newx, newy))
                    res.append((newx, newy))
                    visited.append((newx, newy))
                    cnt += 1
    return cnt

Y, X = map(int, input().split())
mymap = [list(input()) for _ in range(Y)]
ans = 98765432
visited = []
for y in range(Y):
    for x in range(X):
        if mymap[y][x] == 'L' and (x, y) not in visited:
            res = []
            cnt = 0
            BFS(x, y)
            if ans > cnt:
                ans = cnt
print(ans)