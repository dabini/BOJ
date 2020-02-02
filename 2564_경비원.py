X, Y = map(int, input().split())
num = int(input())
field = [[0] * (X+1) for y in range(Y+1)]
cnt = 0
for n in range(num):
    d, a = map(int, input().split())
    if d == 1:
        field[0][a] = 1
    elif d == 2:
        field[Y][a] = 1
    elif d ==3:
        field[a][0] =1
    else:
        field[a][X] =1

d_x, a_x = map(int, input().split())
if d_x == 1:
    i, j = 0, a_x
elif d_x == 2:
    i, j = Y, a_x
elif d_x == 3:
    i, j = a_x, 0
else:
    i, j = a_x, X

for y in range(Y+1):
    for x in range(X+1):
        if field[y][x] == 1:
            if y == i and x == j:
                cnt += 0
            elif y != i and x ==j:
                cnt += abs(i-y)
            elif y == i and x !=j:
                cnt += abs(j-x)
            else:
                cnt += i + j + y
print(cnt)