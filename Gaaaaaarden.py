def gfind(k, g):
    global g_lst, cnt, visited
    if g == G:
        g_lst = []
        cnt = 0
        visited = [[0] * M for _ in range(N)]
        for i in range(len(lst)):
            if used[i]:
                g_lst.append(lst[i])
                # visited[lst[i][1]][lst[i][0]] = 1
        rfind(0, 0)
        glst.append(g_lst)
        return
    if k >= len(lst):
        return
    used[k] = 1
    gfind(k+1, g+1)
    used[k] = 0
    gfind(k+1, g)

def rfind(k, r):
    global r_lst, rlst, g_lst
    if r == R:
        r_lst = []
        for i in range(len(lst)):
            if used[i] and lst[i] not in g_lst:
                r_lst.append(lst[i])
        rlst.append(r_lst)
        flower(g_lst, r_lst)
        return
    if k >= len(lst):
        return
    else:
        if used[k] == 0:
            used[k] = 1
            rfind(k + 1, r+1)
            used[k] = 0
            rfind(k + 1, r)


def flower(g_lst, r_lst):
    global cnt, visited, max_num, res
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ng_lst, nr_lst = [], []
    for g in g_lst:
        gx, gy = g[0], g[1]
        for d in range(4):
            nx,  ny = gx+dx[d], gy+dy[d]
            if 0 <= nx < M and 0 <= ny < N and garden[ny][nx] != 0:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    ng_lst.append([nx, ny])

    for r in r_lst:
        rx, ry = r[0], r[1]
        for d in range(4):
            nx, ny = rx + dx[d], ry + dy[d]
            if 0 <= nx < M and 0 <= ny < N and garden[ny][nx] != 0:
                if not visited[ny][nx]:
                    visited[ny][nx] = 2
                    nr_lst.append([nx, ny])
                elif visited[ny][nx] == 1:
                    cnt += 1

    if not ng_lst and not nr_lst:
        if max_num < cnt:
            max_num = cnt
        return max_num

    for y in range(N):
        for x in range(M):
            if visited[y][x] == 1 or visited[y][x] == 2:
                visited[y][x] = -1
    # for r in r_lst:
    #     visited[r[1]][r[0]] = -1
    # for g in g_lst:
    #     visited[g[1]][g[0]] = -1
    flower(ng_lst, nr_lst)

# def flower(g_lst, r_lst):
#     global cnt, visited, max_num
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     i = 1
#     while True:
#         if i >= N or i >=M:
#             break
#         for g in g_lst:
#             gx, gy = g[0], g[1]
#             visited[gy][gx] = -1
#             for d in range(4):
#                 nx,  ny = gx+dx[d]*i, gy+dy[d]*i
#                 if 0 <= nx < M and 0 <= ny < N and garden[ny][nx] != 0:
#                     if not visited[ny][nx]:
#                         visited[ny][nx] = 1
#         for r in r_lst:
#             rx, ry = r[0], r[1]
#             visited[ry][rx] = -1
#             for d in range(4):
#                 nx,  ny = rx+dx[d]*i, ry+dy[d]*i
#                 if 0 <= nx < M and 0 <= ny < N and garden[ny][nx] != 0:
#                     if not visited[ny][nx]:
#                         visited[ny][nx] = 2
#                     elif visited[ny][nx] == 1:
#                         cnt += 1
#         for y in range(N):
#             for x in range(M):
#                 if visited[y][x] == 1 or visited[y][x] == 2:
#                     visited[y][x] = -1
#
#     if max_num < cnt:
#         max_num = cnt
#     return max_num

N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
lst = []
max_num = -1
for n in range(N):
    for m in range(M):
        if garden[n][m] == 2:
            lst.append([m, n])
glst = []
rlst = []
used = [0] * len(lst)
gfind(0, 0)
print(max_num)
print(rlst)
print(glst)


#해답

import sys
from collections import deque
input = sys.stdin.readline

EMPTY, GREEN, RED, FLOWER = 0, 1, 2, 3
n,m,g,r = 0, 0, 0, 0
board = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cand = [] # 좌표를 담을 에정
candsz = 0
isused = [False]*10
chosen_g = [0]*5
chosen_r = [0]*5
mx = 0

# popleft, append
def solve():
  cnt = 0
  state = [[[0]*2 for i in range(m)] for j in range(n)]
  q = deque()

  for i in range(g):
    state[cand[chosen_g[i]][0]][cand[chosen_g[i]][1]] = [0, GREEN]
    q.append(cand[chosen_g[i]])

  for i in range(r):
    state[cand[chosen_r[i]][0]][cand[chosen_r[i]][1]] = [0, RED]
    q.append(cand[chosen_r[i]])

  while q:
    cur = q.popleft()
    curtime, curcolor = state[cur[0]][cur[1]]
    if state[cur[0]][cur[1]][1] == FLOWER: continue
    for dir in range(4):
      nx = cur[0]+dx[dir]
      ny = cur[1]+dy[dir]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
      if board[nx][ny] == 0: continue
      if state[nx][ny][1] == EMPTY:
        state[nx][ny] = [curtime+1,curcolor]
        q.append([nx,ny])
      elif state[nx][ny][1] == RED:
        if curcolor == GREEN and state[nx][ny][0] == curtime+1:
          cnt += 1
          state[nx][ny][1] = FLOWER
      elif state[nx][ny][1] == GREEN:
        if curcolor == RED and state[nx][ny][0] == curtime+1:
          cnt += 1
          state[nx][ny][1] = FLOWER
  return cnt

def select_r(idx):
  global mx
  if idx == r:
    mx = max(mx, solve())
    return None

  cur = 0
  if idx != 0: cur = chosen_r[idx-1] + 1
  while cur < candsz:
    if isused[cur]:
      cur += 1
      continue
    isused[cur] = True
    chosen_r[idx] = cur
    select_r(idx+1)
    isused[cur] = False
    cur += 1

def select_g(idx):
  if idx == g:
    select_r(0)
    return None

  cur = 0
  if idx != 0: cur = chosen_g[idx-1] + 1
  while cur < candsz:
    isused[cur] = True
    chosen_g[idx] = cur
    select_g(idx+1)
    isused[cur] = False
    cur += 1

n,m,g,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
  for j in range(m):
    if board[i][j] == 2:
      cand.append([i,j])
candsz = len(cand)
select_g(0)
sys.stdout.write(str(mx)+"\n")



#해답 2
import sys
from collections import deque
import itertools

input = sys.stdin.readline

EMPTY, GREEN, RED, FLOWER = 0, 1, 2, 3
n, m, g, r = 0, 0, 0, 0
board = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cand = []  # 좌표를 담을 에정
candsz = 0
chosen_g = [0] * 5
chosen_r = [0] * 5
mx = 0


# popleft, append
def solve():
    cnt = 0
    state = [[[0] * 2 for i in range(m)] for j in range(n)]
    q = deque()

    for i in range(g):
        state[cand[chosen_g[i]][0]][cand[chosen_g[i]][1]] = [0, GREEN]
        q.append(cand[chosen_g[i]])

    for i in range(r):
        state[cand[chosen_r[i]][0]][cand[chosen_r[i]][1]] = [0, RED]
        q.append(cand[chosen_r[i]])

    while q:
        cur = q.popleft()
        curtime, curcolor = state[cur[0]][cur[1]]
        if state[cur[0]][cur[1]][1] == FLOWER: continue
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == 0: continue
            if state[nx][ny][1] == EMPTY:
                state[nx][ny] = [curtime + 1, curcolor]
                q.append([nx, ny])
            elif state[nx][ny][1] == RED:
                if curcolor == GREEN and state[nx][ny][0] == curtime + 1:
                    cnt += 1
                    state[nx][ny][1] = FLOWER
            elif state[nx][ny][1] == GREEN:
                if curcolor == RED and state[nx][ny][0] == curtime + 1:
                    cnt += 1
                    state[nx][ny][1] = FLOWER
    return cnt


n, m, g, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            cand.append([i, j])
candsz = len(cand)

for c1 in itertools.combinations(range(candsz), g + r):
    for c2 in itertools.combinations(range(g + r), g):
        ridx, gidx = 0, 0
        for i in range(g + r):
            if i in c2:
                chosen_g[gidx] = c1[i]
                gidx += 1
            else:
                chosen_r[ridx] = c1[i]
                ridx += 1
        mx = max(mx, solve())

sys.stdout.write(str(mx) + "\n")