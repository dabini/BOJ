#수정 필요..
n, m = map(int, input().split())

a = [0] * m
ans = []
def backtrack(index, n, m):
    if index == m:
        res = []
        for i in range(m):
            res.append(a[i])
        if res[::-1] not in ans:
            ans.append(res)
    else:
        for i in range(1, n + 1):
            a[index] = i
            backtrack(index + 1, n, m)

backtrack(0, n, m)
for a in ans:
    print(*a)