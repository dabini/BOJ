# from collections import deque
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# def BFS(x, y):
#     q= deque([(x, y)])
#     visited = set([(x, y)])
#     time = 0
#     shark = 2
#     cnt = 0
#     status = False
#
#     tmp = 0
#
#     while q:
#         size =  len(q)
#
#         q = deque(sorted(q)) #위, 왼 쪽을 먼저 가야하기 때문에 sorted해줘야함!!
#         for s in range(size):
#             x, y = q.popleft()
#
#             if arr[y][x] and arr[y][x] < shark:
#                 arr[y][x] = 0
#                 cnt += 1
#
#                 if cnt == shark:
#                     shark += 1
#                     cnt = 0
#
#                 q = deque()
#                 visited = set([(x, y)])
#                 status = True
#
#                 tmp = time
#
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0<= nx <N and 0<= ny <N and (nx, ny) not in visited:
#                     if arr[ny][nx] <= shark:
#                         q.append((nx, ny))
#                         visited.add((nx, ny))
#
#             if status:
#                 status = False
#                 break
#
#         time += 1
#     return tmp
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# sharkx, sharky = None, None
# for y in range(N):
#     for x in range(N):
#         if arr[y][x] == 9:
#             sharkx, sharky = x, y
#             arr[y][x] = 0
#
# print(BFS(sharkx, sharky))

# from collections import deque
# dxs = [-1, 0, 0, 1]
# dys = [0, -1, 1, 0]
# def bfs(x, y):
#     q, visited = deque([(x, y)]), set([(x, y)])
#     time = 0
#     shark = 2 # 현재 아기 상어의 크기다.
#     eat = 0 # 현재 크기에서, 지금까지 먹은 물고기 수다.
#     eat_flag = False # 현재 상태에서 물고기를 먹은 경우, # for _ in range(size) 구문을 진행하지 않기 위한 플래그다.
#     answer = 0
#     while q:
#         size = len(q) # 위, 그리고 왼쪽을 더 우선시해서 가야하기 때문에, BFS queue를 소팅해준다.
#         q = deque(sorted(q))
#         for _ in range(size):
#             x, y = q.popleft() # 현재 위치에 아기 상어보다 작은 물고기가 있어서, 이를 먹은 경우.
#             if board[x][y] != 0 and board[x][y] < shark:
#                 board[x][y] = 0
#                 eat += 1 # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해줘야한다.
#
#                 if eat == shark:
#                     shark += 1
#                     eat = 0 # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문에, # BFS queue 와 visited 를 초기화 해준다.
#
#                 q, visited = deque(), set([(x, y)])
#                 eat_flag = True # 먹었을 때의 시간을 저장해둔다.
#                 answer = time
#             for dx, dy in zip(dxs, dys):
#                 nx, ny = x + dx, y + dy
#                 if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
#                     if board[nx][ny] <= shark:
#                         q.append((nx, ny))
#                         visited.add((nx, ny)) # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
#
#             if eat_flag:
#                 eat_flag = False
#                 break
#         time += 1
#     return answer
# n = int(input())
# board = [list(map(int , input().split())) for _ in range(n)]
# # 1. 초기 상어(자신)의 위치를 파악하고, 해당 자리는 판에서 비워둔다.
# s_x, s_y = None, None
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 9:
#             s_x, s_y = i, j
#             board[i][j] = 0
#
# # 2. 시작점에서 BFS 진행
# print(bfs(s_x, s_y))

def start(i, j):
    global N, arr, size, cnt, res, ti, tj
    check = [[0 for _ in range(N)] for _ in range(N)]
    queue = []
    queue.append([i, j])
    check[i][j] = 1

    fish = []
    while queue:
        i, j = queue.pop(0)
        for x, y in [[-1,0],[0,-1],[0,1],[1,0]]:
            ni, nj = i + x, j + y
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] <= size and not check[ni][nj]:
                    check[ni][nj] = check[i][j] + 1
                    queue.append([ni, nj])
                    if 0 < arr[ni][nj] < size:
                        fish.append([check[ni][nj], ni, nj])

    if fish:
        fish.sort()
        res += (fish[0][0] - 1)
        arr[fish[0][1]][fish[0][2]] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        start(fish[0][1], fish[0][2])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2

ti, tj = 0, 0
x, y = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            arr[i][j] = 0
cnt = 0
res = 0
start(x, y)
print(res)