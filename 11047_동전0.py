N, K = map(int, input().split())
coin_list = []
for n in range(N):
    coin_list += [int(input())]

cnt = 0
i = N-1
while K:
    tmp = 0
    if coin_list[i] <= K:
        tmp += K // coin_list[i]
        K -= coin_list[i] * (tmp)
    i -= 1
    cnt += tmp

    if K == 0:
        break

print(cnt)
