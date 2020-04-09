def backtracking(a, r):
    if r == 0:
        print(*res)
        return
    for i in range(a, k):
        res.append(lst[i])
        visited[lst[i]] = 1
        backtracking(i+1, r-1)
        res.pop()
        visited[lst[i]] = 0

while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    k = lst.pop(0)
    lst = list(map(int, lst))
    visited = [0] * 50
    res = []
    backtracking(0, 6)
    print()