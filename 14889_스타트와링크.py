import sys
from itertools import combinations


input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for n in range(N)]
# print(arr)


# 조합 구하기
lst = [i for i in range(N)]
res = 987654321
for i in list(combinations(lst, N//2)):
    s_score = 0
    l_score = 0
    link = []
    for j in lst:
        if j not in i:
            link.append(j)
    for x, y in list(combinations(i, 2)):
        s_score += arr[x][y] + arr[y][x]
    for a, b, in list(combinations(link, 2)):
        l_score += arr[a][b] + arr[b][a]
    res = min(res, abs(s_score - l_score))

print(res)