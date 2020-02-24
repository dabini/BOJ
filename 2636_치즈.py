import sys
sys.setrecursionlimit(10**8)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(y, x, visited):
    global X, Y
    for d in range(4):
        newy = y + dy[d]
        newx = x + dx[x]
        if 0 < newy < Y-1 and 0 < newx < X-1 and (newy, newx) not in visited and (cheese[newy][newx] == 0 or cheese[newy][newx] == -1):
            DFS(newy,newx,visited)
        cheese[y][x] = -1

def melted(y, x, visited):
    visited.add((y, x))

    check = False
    for d in range(4):
        newy = y + dy[d]
        newx = x + dx[x]
        if cheese[newy][newx] == -1:
            check = True
            break

    for d in range(4):
        newy = y + dy[d]
        newx = x + dx[x]
        if 0 < newy < Y and 0 < newx < X and (newy,newx) not in visited and cheese[newy][newx] == 1:
            melted(newy, newx, visited)

    if check:
        cheese[y][x] = -1

    return visited
Y, X = map(int, input().split())
cheese = [list(map(int, input().split()))for _ in range(Y)]

melt = False
time = 0
visited = None
while not melt:
    DFS(0, 0, set())
    visited = set()

    for y in range(Y):
        for x in range(X):
            if cheese[y][x] == 1 and (y, x) not in visited:
                visited |= melted(y, x, set())
    time += 1

    melt = True
    for y in range(Y):
        for x in range(X):
            if cheese[y][x] == 1:
                melt = False
print(time)
print(len(visited))

