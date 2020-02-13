num = int(input())
atm = list(map(int, input().split()))
atm.sort()
total = 0
for n in range(num):
    mid = 0
    for m in range(0, n+1):
        mid += atm[m]
    total += mid

print(total)
