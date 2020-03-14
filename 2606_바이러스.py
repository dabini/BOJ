def Find(a):
    global cnt
    visited.append(a)
    for now in range(num+1):
        if arr[a][now] and now not in visited:
            cnt += 1
            Find(now)
        return

num = int(input())
arr = [[0] * (num+1) for _ in range(num+1)]
visited = []
cnt = 0
for _ in range(int(input())):
    start, end = map(int, input().split())
    arr[start][end] = 1
Find(1)
print(cnt)