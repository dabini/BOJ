N = int(input())
field = [[0]*101 for _ in range(101)]

for n in range(N):
    shark_x, Y = map(int, input().split())

    for y in range(Y, Y+10):
        for x in range(shark_x, shark_x + 10):
            field[y][x] = 1

cnt = 0
for j in range(101):
    for i in range(101):
        if field[j][i] ==1:
            cnt += 1
print(cnt)