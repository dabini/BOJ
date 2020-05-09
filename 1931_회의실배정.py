import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lst.append((start, end))
lst.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_time = lst[0][1]
for n in range(1, N):
    if lst[n][0] >= end_time:
        cnt += 1
        end_time = lst[n][1]
print(cnt)