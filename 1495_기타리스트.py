import sys
input = sys.stdin.readline


## 배열 하나 사용
def find():
    arr = [[0]*(M+1) for _ in range(N+1)]
    arr[0][S] = 1

    for i in range(1, N+1):
        for j in range(M+1):
            if arr[i-1][j]:
                if j + volumes[i-1] <= M:
                    arr[i][j+volumes[i-1]] = 1
                if j - volumes[i-1] >= 0:
                    arr[i][j - volumes[i-1]] = 1
    for i in range(M, -1, -1):
        if arr[-1][i]:
            return i
    return -1

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))
print(find())


# 리스트 2개 사용

# N, S, M = map(int, input().split())
# volumes = list(map(int, input().split()))
#
# lst = [0 for _ in range(M+1)]
# lst2 = [0 for _ in range(M+1)]
#
# lst[S] = 1
#
# for v in volumes:
#     for m in range(M+1):
#         if lst[m]:
#             if v + m <= M:
#                 lst2[v+m] = 1
#             if m - v >= 0:
#                 lst2[m-v] = 1
#     lst = lst2
#     lst2 = [0] * (M+1)
#
# res = -1
# for i in range(M, -1, -1):
#     if lst[i]:
#         res = i
#         break
# print(res)