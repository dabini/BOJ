import sys


input = sys.stdin.readline
N, M = map(int, input().split())
height_list = list(map(int, input().split()))
height_list.sort()
start = 1
end = max(height_list)

while start <= end:
    mid = (start+end) //2
    ans = 0
    for h in height_list:
        if h > mid:
            ans += h - mid
        if ans >= M:
            break
    if ans >= M:
        start = mid + 1
    else:
        end = mid -1
print(end)