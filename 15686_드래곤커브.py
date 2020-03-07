'''
0세대 일때 1번 = 1
1세대 일 때 2의 0승 = 1 +1 =  2
2세대 2의 1승 = 2 + 1 + 1 = 4
3세대 2의 2승 = 4 + 2 + 1 + 1 = 8
4세대 2의 3승 = 8  + 4 + 2 + 1 + 1 = 16
'''

def check(x, y, d, now):
    global g
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    board[y][x] = 1
    lst = []

    while True:
        if now == g:
            break
        ny = y + dy[d]
        nx = x + dx[d]
        board[ny][nx] = True
        y = ny
        x = nx
        if now in find:
            lst = lst[::-1]
            d = (d + 1) % 4

N = int(input())
board = [[0]* 100 for _ in range(100)]
res = 0
find = [0] + [2**a for a in range(10)]
for n in range(N):
    x, y, d, g = map(int, input().split())
    check(x, y, d, 0)


for j in range(99):
    for i in range(99):
        if board[j][i]:
            if board[j][i+1] and board[j+1][i] and board[j+1][i+1]:
                res += 1
print(res)