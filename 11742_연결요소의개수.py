import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def DFS(n):
    visited[n] = 1
    for i in arr[n]:
        if not visited[i]:
            DFS(i)

N, M= map(int, input().split())
arr= [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
visited = [0 for _ in range(N+1)]
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        cnt += 1
print(cnt)