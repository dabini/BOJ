def BFS(a):
    q= [a]
    res = [a]
    while q:
        now = q.pop()
        for new in range(num +1):
            if arr[new][now] and new not in res:
                res.append(new)
                q.append(new)
    return len(res)
num = int(input())
arr = [[0] * (num+1) for _ in range(num+1)]
visited = []
cnt = 0
for _ in range(int(input())):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1
print(BFS(1) -1)