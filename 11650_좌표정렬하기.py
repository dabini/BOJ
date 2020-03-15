N = int(input())
lst = []
for n in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort()
for l in lst:
    print(l[0], l[1])
