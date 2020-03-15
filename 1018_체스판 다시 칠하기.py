def Check(x, y):
    global cnt, min_num
    color = ["B", "W"]
    for c in range(2):
        cnt = 0
        for j in range(y, y+8):
           for i in range(x, x+8):
               if chess[j][i] != color[c%2]:
                   cnt += 1
               c += 1
           c += 1
        if cnt < min_num:
            min_num = cnt
    return min_num


N, M = map(int, input().split())
chess = [list(map(str, input())) for _ in range(N)]
min_num = 98765432
for y in range(N-7):
    for x in range(M-7):
        Check(x, y)
print(min_num)