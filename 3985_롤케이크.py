L = int(input())
lst = [0] * (L+1)
N = int(input())
max_num = -1
max_cnt = 0
for n in range(N):
    p, k = map(int, input().split())
    for i in range(p, k+1):
        if lst[i] == 0:
            lst[i] = n+1
    if max_num < k-p:
        max_num = k-p
        res = n+1

for i in range(1, N+1):
    if max_cnt < lst.count(i):
        max_cnt = lst.count(i)
        res2 = i
# print(lst)
print(res)
print(res2)