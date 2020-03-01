def backtracking(N, M, K, l):
    if N == K:
        print(*res)
        return
    else:
        for i in range(M):
            if visited[i] == 0 and l < lst[i]:
                visited[i] = 1
                l = lst[i]
                res[N] = lst[i]
                backtracking(N+1, M, K, l)
                visited[i] = 0

N, M = map(int, input().split())

lst = range(1, N+1)
visited = [0] *N
res = [0]* M
backtracking(0, N, M, 0)