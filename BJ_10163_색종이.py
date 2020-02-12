# 가장 왼쪽 아래 칸의 번호와 너비, 높이
T = int(input())

a = [[0] * 101 for i in range(101)]
# print(a)
for t in range(1, T+1):
    x, y, w, h = map(int, input().split())

    for i in range(x, x+w):
        for j in range(y, h+y):
            a[j][i] = t

check = [0] * (T+1)
for i in range(101):
    for j in range(101):
        check[a[i][j]] += 1

for i in check[1:]:
    print(i)