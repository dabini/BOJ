def bfs(start, end):
    q = deque()
    q.append(start)
    visited = set()
    while q:
        x = q.popleft()
        visited.add(x)
        next = arr[x]
        for j in range(len(next)):
            if next[j] == 1:
                if j == end:
                    return 1
                elif j not in visited:
                    q.append(j)
                    visited.add(j)
    return 0
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(N)]

check = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        check[y][x] = bfs(y, x)
    print(*check[y])