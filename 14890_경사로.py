# def find(x, y):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     for d in range(4):
#         ny = y + dy[d]
#         nx = x + dx[d]
#         if 0<= nx < N and 0 <= ny <N:
#
#     dix = [-2, 2, -2, 2]
#     diy = [-1, -1, 1, 1]


# def slope(i, c):
#     global ans
#     cnt = 1
#     for j in range(0, N-1):
#         d = a[i][j+1]-a[i][j] if c else a[j+1][i]-a[j][i]
#         if d == 0:
#             cnt += 1
#         elif d == 1 and cnt >= L:
#             cnt = 1
#         elif d == -1 and cnt >= 0:
#             cnt = -L+1
#         else:
#             return
#     if cnt >= 0:
#         ans += 1
#
# def solve():
#     for i in range(N):
#         slope(i, 1)
#         slope(i, 0)
#     print(ans)
#
# N, L = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# solve()
#
# def find(c):
#     global res
#     cnt = 1
#     for j in range(N):
#         for i in range(N-1):
#             if c:
#                 d = mymap[j][i+1] - mymap[j][i]
#             else:
#                 d = mymap[j+1][i] - mymap[j][i]
#
#             if d == 0:
#                 cnt += 1
#             elif d == 1 and cnt >= L:
#                 cnt = 1
#             elif d == -1 and cnt >= 0:
#                 cnt = -L+1
#             else:
#                 return
#     if cnt >= 0:
#         res += 1

def find(lst):
    i = 0
    check = 1
    now = lst[i]
    while i < N-1 :
        i += 1
        d = now - lst[i]
        if d >1 or d < -1: #1이상 차이날 때
            return False
        elif d == 1:
            if i+L > N: #범위 벗어날 때
                return False
            for k in range(i+1, i+L): #범위내에서
                if now - lst[k] != 1:
                    return False
            check = 1-L
        elif d == -1:
            if i-L < 0 or check < L:
                return False
            check = 1
        else:
            check += 1

        now = lst[i]
    return True


N, L = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for m in mymap:
    if find(m):
        cnt += 1

for j in range(N):  #전치행렬 만들기
    for i in range(N):
        if i > j:
            mymap[j][i], mymap[i][j] = mymap[i][j], mymap[j][i]

for m in mymap:
    if find(m):
        cnt += 1
print(cnt)