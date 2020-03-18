# def find(x, y, n):
#     global check, lst, max_num
#     max_num = 0
#     if n == 1:
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
#         for d in range(4):
#             nx, ny = x, y
#             check = 0
#             while True:
#                 nx += dx[d]
#                 ny += dy[d]
#                 if ny < 0 or ny >= N or nx < 0 or nx >=N or cctv[ny][nx] == 6:
#                     break
#                 else:
#                     if (nx, ny) not in lst:
#                         lst.append((nx, ny))
#                         check += 1
#             if max_num < check:
#                 max_num = check
#     elif n == 2:
#         dx = [1, 0]
#         dy = [0 ,1]
#         for d in range(2):
#             nx, ny = x, y
#             nx2, ny2 = x, y
#             check = 0
#             while True:
#                 nx += dx[d]
#                 ny += dy[d]
#                 nx2 -= dx[d]
#                 ny2 -= dy[d]
#                 if ny < 0 or ny >= N or nx < 0 or nx >=N:
#                     break
#                 elif cctv[ny][nx] == 6 or cctv[ny2][nx2]:
#                     continue
#                 elif (nx, ny) not in lst:
#                     lst.append((nx, ny))
#                     check += 1
#                     pass
#                 elif (nx2, ny2) not in lst:
#                     lst.append((nx2, ny2))
#                     check += 1
#             if max_num < check:
#                 max_num = check
#     elif n == 3:
#         dx = [1, 1, -1, -1]
#         dy = [1, -1, 1, -1]
#         for d in range(4):
#             nx, ny = x, y
#             check = 0
#             while True:
#                 nx += dx[d]
#                 ny += dy[d]
#                 if ny < 0 or ny >= N or nx < 0 or nx >= N:
#                     break
#                 elif cctv[y][nx] == 6:
#                     continue
#                 elif (x, ny) not in lst:
#                         lst.append((x, ny))
#                         check += 1
#                 elif (nx, y) not in lst:
#                         lst.append((nx, y))
#                         check += 1
#             if max_num < check:
#                 max_num = check
#     elif n == 4:
#
#     elif n == 5:
#         check = 0
#         nx, ny = x, y
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
#         for d in range(4):
#             nx, ny = x, y
#             while True:
#                 nx += dx[d]
#                 ny += dy[d]
#                 if ny < 0 or ny >= N or nx < 0 or nx >= N or cctv[ny][nx] == 6:
#                     break
#                 else:
#                     if (nx, ny) not in lst:
#                         lst.append((nx, ny))
#                         check += 1
#             max_num = check
#
#
#
#
# N, M = map(int, input().split())
# cctv = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# ans = 0
# lst = []
# for j in range(N):
#     for i in range(M):
#         if cctv[j][i] == 0:
#             ans += 1
#         if cctv[j][i] >0 and cctv[j][i] <=5:
#             min_num = 987654321
#             find(i, j, cctv[j][i])
#             cnt += max_num
# print(ans - cnt)

def search(max, cctv, maps):
    global min_num
    if max >= len(cctv):
        count = 0
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 0:
                    count += 1
        min_num = min(min_num, count)
        return

    if cctv[max][0] == 1:
        for i in range(len(dx)):
            x, y = cctv[max][1], cctv[max][2]
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                temp = []
                for j in range(N):
                    temp.append([])
                    for k in range(M):
                        temp[j].append(maps[j][k])
                while 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                    # print(x+dx[i], y+dy[i])
                    if temp[x + dx[i]][y + dy[i]] == 6:
                        break
                    elif temp[x + dx[i]][y + dy[i]] == 0:
                        temp[x + dx[i]][y + dy[i]] = '#'
                    x += dx[i]
                    y += dy[i]
                search(max + 1, cctv, temp)

    elif cctv[max][0] == 2:
        for i in range(0, 2):
            temp = []
            for k in range(N):
                temp.append([])
                for l in range(M):
                    temp[k].append(maps[k][l])
            for j in range(i, len(dx), 2):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x + dx[j] < N and 0 <= y + dy[j] < M:
                    if temp[x + dx[j]][y + dy[j]] == 6:
                        break
                    elif temp[x + dx[j]][y + dy[j]] == 0:
                        temp[x + dx[j]][y + dy[j]] = '#'
                    x += dx[j]
                    y += dy[j]
            search(max + 1, cctv, temp)

    elif cctv[max][0] == 3:
        for i in range(len(dx)):
            temp = []
            for k in range(N):
                temp.append([])
                for l in range(M):
                    temp[k].append(maps[k][l])
            for j in range(i, i + 2):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x + dx[j % 4] < N and 0 <= y + dy[j % 4] < M:
                    if temp[x + dx[j % 4]][y + dy[j % 4]] == 6:
                        break
                    elif temp[x + dx[j % 4]][y + dy[j % 4]] == 0:
                        temp[x + dx[j % 4]][y + dy[j % 4]] = '#'
                    x += dx[j % 4]
                    y += dy[j % 4]
            search(max + 1, cctv, temp)

    elif cctv[max][0] == 4:
        for i in range(len(dx)):
            temp = []
            for k in range(N):
                temp.append([])
                for l in range(M):
                    temp[k].append(maps[k][l])
            for j in range(i, i + 3):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x + dx[j % 4] < N and 0 <= y + dy[j % 4] < M:
                    if temp[x + dx[j % 4]][y + dy[j % 4]] == 6:
                        break
                    elif temp[x + dx[j % 4]][y + dy[j % 4]] == 0:
                        temp[x + dx[j % 4]][y + dy[j % 4]] = '#'
                    x += dx[j % 4]
                    y += dy[j % 4]
            search(max + 1, cctv, temp)

    elif cctv[max][0] == 5:
        temp = []
        for j in range(N):
            temp.append([])
            for k in range(M):
                temp[j].append(maps[j][k])
        for i in range(len(dx)):
            x, y = cctv[max][1], cctv[max][2]
            while 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if temp[x + dx[i]][y + dy[i]] == 6:
                    break
                elif temp[x + dx[i]][y + dy[i]] == 0:
                    temp[x + dx[i]][y + dy[i]] = '#'
                x += dx[i]
                y += dy[i]
        search(max + 1, cctv, temp)


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cctv = []
min_num = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append([arr[i][j], i, j])
        if arr[i][j] == 0:
            min_num += 1
search(0, cctv, arr)
print(min_num)