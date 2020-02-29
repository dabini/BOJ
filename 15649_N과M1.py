def permutations(prefix,k):
    if len(prefix) == M:
        yield prefix
    else:
        for i in range(k,len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]

N, M = map(int, input().split())
arr = list(range(1, N+1))
res = []
for perm in permutations([],0):
    res.append(perm)
res.sort()
for r in res:
    print(*r)