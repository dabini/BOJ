max_x, max_y = map(int, input().split())

field = [[0]*max_x for _ in range(max_y)]

cut_num = int(input())

for cut in range(cut_num):
    a, b = map(int, input().split())
    new_x = []
    new_y = []
    if a == 0: # 가로
        new_x.append(b)
    elif a == 1: #세로
        new_y.append(b)

    for

