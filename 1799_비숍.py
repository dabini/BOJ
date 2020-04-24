import sys
input = sys.stdin.readline

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
right = [[0] * n for _ in range(n)]
left = [[0] * n for _ in range(n)]
r, l = 1, 1


for i in range(n):
    j = 0
    while j<n and 0<=i:
        if chess[j][i]:
            right[j][i] = r
        j += 1
        i -= 1
    r += 1

for j in range(1, n):
    i = n-1
    while j<n and 0<= i:
        if chess[j][i]:
            right[j][i] = r
        j += 1
        i -= 1
    r += 1

for i in range(n-1, -1, -1):
    j = 0
    while j<n and i<n:
        if chess[j][i]:
            left[j][i] = l
        j += 1
        i += 1
    l += 1

for j in range(1, n):
    i = 0
    while j <n and i<n:
        if chess[j][i]:
            left[j][i] = l
        j += 1
        i += 1
    l += 1

arr = [[] for _ in range(l)]
for y in range(n):
    for x in range(n):
        if chess[y][x]:
            arr[left[y][x]].append(right[y][x])

def dfs(idx):
    visited[idx] = 1
    l = arr[idx]
    for i in l:
        if RtoL[i] == 0 or (not visited[RtoL[i]] and dfs(RtoL[i])):
            RtoL[i] = idx
            LtoR[idx] = i
            return True
    return False

LtoR = [0] * (n*2)
RtoL = [0] * (n*2)
res = 0

for i in range(1, 2*n):
    visited = [0] * (2*n)
    if dfs(i):
        res += 1
print(res)



# # 1<= l, r <=2*n
# link = [[] for _ in range(l)]
# for i in range(n):
#     for j in range(n):
#         if chess[i][j]:
#             link[left[i][j]].append(right[i][j])
#
# def dfs(idx):
#     visited[idx] = True
#     l = link[idx]
#     for p in l:
#         if r2l[p] == 0 or (not visited[r2l[p]] and dfs(r2l[p])):
#             r2l[p] = idx
#             l2r[idx] = p
#             return True
#     return False
#
# l2r = [0] * (2*n)
# r2l = [0] * (2*n)
# ans = 0
# for i in range(1, 2*n):
#     visited = [False] * (2*n)
#     if dfs(i):
#         ans += 1
# print(ans)
