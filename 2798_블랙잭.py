N, M = map(int, input().split())
lst = list(map(int, input().split()))
res = 0
for i in lst:
    for j in lst:
        for k in lst:
            if i !=j and i != k and j != k:
                if i+j+k <= M and i+j+k >res:
                    res = i+j+k
print(res)
