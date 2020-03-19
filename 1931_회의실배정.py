N = int(input())
lst = []
for _ in range(N):
    start, end = map(int, input().split())
    lst.append((start, end))
for n in range(N):
    max_num = 0
    for m in range(n+1, M):
