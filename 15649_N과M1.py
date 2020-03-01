# def permutations(prefix,k):
#     if len(prefix) == M:
#         yield prefix
#     else:
#         for i in range(k,len(arr)):
#             arr[i], arr[k] = arr[k], arr[i]
#             for next in permutations(prefix + [arr[k]], k+1):
#                 yield next
#             arr[i], arr[k] = arr[k], arr[i]
#
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
# res = []
# for perm in permutations([],0):
#     res.append(perm)
# res.sort()
# for r in res:
#     print(*r)

n, m = map(int, input().split())

check = [False] * (n + 1)
a = [0] * m

def backtrack(index, n, m):
    if index == m:
        res = []
        for i in range(m):
            res.append(a[i])
        return print(*res)

    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        backtrack(index + 1, n, m)
        check[i] = False
backtrack(0, n, m)