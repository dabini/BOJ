import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([y, x])

lst.sort()
for l in lst:
    print(l[1], l[0])