# from collections import deque
#
# def find(x, y, n):
#     global ans, res
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     for d in range(4):
#         ny = y + dy[d]
#         nx = x + dx[d]
#         if 0<= ny < N and 0 <= nx < N and  arr[ny][nx] <= n:
#             res += 1
#             if 0 < arr[ny][nx] <= n and (ny,nx) not in visited:
#                 q.append((ny,nx))
#                 visited.append((ny, nx))
#                 if ans < n:
#                     ans += 1
#                     find(nx, ny, n)
#                 elif ans == n:
#                     ans = 0
#                     n += 1
#                     find(nx, ny, n)
#     visited.pop()
#     return
#
#
#     # for j in range(N):
#     #     for i in range(N):
#     #         if 0 < arr[j][i] <= n and (j,i) not in visited:
#     #             visited.append((j, i))
#     #             if ans < n:
#     #                 ans += 1
#     #                 find(i, j, n)
#     #             elif ans == n:
#     #                 ans = 0
#     #                 n += 1
#     #                 find(i, j, n)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# res = 0
# visited = []
# q = deque()
#
# for y in range(N):  #아기 상어 위치 정해주고 0으로 초기화
#     for x in range(N):
#         if arr[y][x] == 9:
#             x, y, n = x, y, 2
#             arr[y][x] = 0
#
# find(x, y, n)
# print(res)

def f(N, size):
    global fishI
    global fishJ
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    minV = 0
    q = []
    visited = [[0]*N for _ in range(N)]
    # 최소 거리의 물고기를 표시할 배열
    checked = [[0]*N for _ in range(N)]
    q.append(fishI)
    q.append(fishJ)
    # 처음 만나는 물고기의 거리 저장
    visited[fishI][fishJ] = 1
    while(len(q)!=0):
        i = q.pop(0)
        j = q.pop(0)
        # 상어가 checked에 기록안된, 먹을 수 있는 물고기를 만나면
        if checked[i][j] == 0 and 0<sea[i][j]<size:
            ## 최초인경우, 최소 거리로 저장하고 checked에 기록
            if minV == 0:
                minV = visited[i][j]
                checked[i][j] = minV
            ## 최초는 아니지만 최소 거리와 같은 거리인 경우
            ### checked에 거리 기록
            elif visited[i][j] == minV:
                checked[i][j] = minV
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if sea[ni][nj]<=size and visited[ni][nj]==0:
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = visited[i][j] + 1
	# checked를 왼쪽 위부터 탐색해서 최초로 0이 아닌 칸을 만나면 거리 정보
    ## 0이 아닌 칸이 없으면 0 리턴
    for i in range(N):
        for j in range(N):
            if checked[i][j] != 0:
                fishI = i
                fishJ = j
                sea[i][j] = 0
                return checked[i][j]-1
    return 0


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

size = 2
fishI = 0
fishJ = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            fishI = i
            fishJ = j
            sea[i][j] = 0
r = 1
sec = 0
eatCnt = 0
while(r!=0):
  	# 물고기를 먹는데 걸린 시간 리턴
    r = f(N, size)
    sec += r
    # 물고기를 먹었으면
    if r!=0:
        eatCnt += 1
        ## 몸집만큼 먹었으면
        if eatCnt == size:
          ### 아기상어 크기 1 증가, 먹은 물고기 수 초기화
            size += 1
            eatCnt = 0
print(sec)