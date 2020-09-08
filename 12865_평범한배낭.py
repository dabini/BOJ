N, K = map(int, input().split())
res = [-1 for _ in range(K+1)]
res[0]= 0
lst = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(K-lst[i][0], -1, -1):
        if res[j] == -1:
            continue
        else:
            res[lst[i][0]+j] = max(res[j]+lst[i][1], res[lst[i][0]+j])
print(max(res))