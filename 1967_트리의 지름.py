from collections import deque
import sys

def bfs(sup):
    q = deque()
    q.append(sup)
    visited = [-1 for _ in range(N+1)]
    visited[sup] = 0

    while q:
        now = q.popleft()
        for next, num in arr[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + num
                q.append(next)
    if check == False:
        return visited.index(max(visited))
    else:
        return max(visited)

input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for n in range(N-1):
    sup, sub, num = map(int, input().split())
    arr[sup].append([sub, num])
    arr[sub].append([sup, num])
print(arr)
check = False
tmp= bfs(1)
check = True
print(bfs(tmp))