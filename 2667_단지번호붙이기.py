dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = []
def find(y, x):
    global num, dx, dy
    mymap[y][x] = 0
    num += 1
    for d in range(4):
        newy = y + dy[d]
        newx = x + dx[d]
        if 0 <= newy < N and 0<= newx < N:
            if mymap[newy][newx] == 1:
                find(newy, newx)
N = int(input())
mymap = [list(map(int, input())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if mymap[y][x] == 1:
            num = 0
            find(y, x)
            res.append(num)

print(len(res))
res.sort()
for i in res:
    print(i)