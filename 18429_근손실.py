from itertools import permutations

N, K = map(int, input().split())
kit = list(map(int, input().split()))
res = 0
lst = []
for day in list(permutations(kit)):
    w = 500
    check = True
    for d in day:
        if w - K + d < 500:
            check = False
            break
        else:
            w += d-K
    if check:
        res += 1
print(res)
