N = int(input())
res = []
for n in range(N):
    res.append(int(input()))

for i in range(len(res)):
    min_num = res[i]
    for j in range(i+1, len(res)):
        if min_num > res[j]:
            min_num = res[j]
            res[i], res[j] = res[j], res[i]

for r in res:
    print(r)