N = int(input())
res = 0

for n in range(1, N):
    total = n
    new = str(n)
    for s in range(len(new)):
        total += int(new[s])
    if total == N:
        res = n
        break

print(res)