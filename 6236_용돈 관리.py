import sys


input = sys.stdin.readline
N, M = map(int, input().split())
lst = []
for n in range(N):
    lst.append(int(input()))
start = 1
end = sum(lst)

while start <= end:
    mid = (start+end) // 2
    ans = 0
    cnt = 1
    for i in range(N):
        if ans + lst[i] > mid:
            ans = 0
            cnt += 1
        ans += lst[i]

    if ans != 0:
        cnt += 1
    if cnt <= M:
        end = mid - 1
    else:
        start = mid + 1
print(end)