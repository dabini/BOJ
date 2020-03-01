n, m = map(int, input().split())

a = [0] * m

def backtrack(index, n, m):
    if index == m:
        res = []
        for i in range(m):
            res.append(a[i])
        return print(*res)

    for i in range(1, n + 1):
        a[index] = i
        backtrack(index + 1, n, m)
backtrack(0, n, m)