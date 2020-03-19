def subset():
    if len(res) == M:
        print(*res)
        return
    if res:
        start = num_lst.index(res[-1])
    else:
        start = 0

    for next in range(start, N):
        res.append(num_lst[next])
        subset()
        res.pop()

N, M = map(int, input().split())
num_lst = list(range(1, N+1))
res = []
subset()