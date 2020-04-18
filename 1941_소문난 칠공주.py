import sys
from itertools import combinations
input = sys.stdin.readline

def check(s):
    soms = 0
    for l in s:
        if seats[l] == "S":
            soms += 1
    if soms < 4: #조합 중에서 S가 4개 미만일 때
        return False
    else:
        for l in s:
            if bfs(l//5, l%5):
                return True
            else:
                return False
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(i, j):
    q =[]
    global a, s
    visited = [0 for _ in range(25)]
    q.append([i, j])
    visited[i*5+j] = 1

    while q:
        x, y = q.pop()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and nx*5+ny in s and not visited[nx*5+ny]:
                q.append([nx, ny])
                visited[nx*5+ny] = 1
    if sum(visited) == 7:
        return True
    else:
        return False

seats = []
for i in range(5):
    seats += list(input().strip())

cnt = 0
for s in combinations(list(i for i in range(25)), 7):
    if check(s):
        cnt += 1
print(cnt)