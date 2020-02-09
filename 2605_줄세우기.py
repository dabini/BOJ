N = int(input())
lst = list(map(int, input().split()))
res = []
for n in range(1, N+1):
    res.insert(n -1 - lst[n-1], n)
print(*res)