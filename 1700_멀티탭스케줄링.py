import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().split()))
check = []
res = 0

for i in range(K):
    max_idx = 0
    if lst[i] not in check:
        if len(check) < N:
            check.append(lst[i])
            lst[i] = 0
        else:
            for c in range(N):
                if lst.count(check[c]) == 0:
                    d = check[c]
                    break
                else:
                    if max_idx < lst.index(check[c]):
                        max_idx = lst.index(check[c])
                        d = lst[max_idx]
            check.remove(d)
            res += 1
            check.append(lst[i])
            lst[i] = 0

    else:
        lst[i] = 0
        continue
print(res)