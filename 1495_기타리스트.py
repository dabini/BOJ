import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

lst = [0 for _ in range(M+1)]
lst2 = [0 for _ in range(M+1)]

lst[S] = 1

for v in volumes:
    for m in range(M+1):
        if lst[m]:
            if v + m <= M:
                lst2[v+m] = 1
            if m - v >= 0:
                lst2[m-v] = 1
    lst = lst2
    lst2 = [0] * (M+1)

res = -1
for i in range(M, -1, -1):
    if lst[i]:
        res = i
        break
print(res)