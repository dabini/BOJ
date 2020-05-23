import sys


input = sys.stdin.readline
N = int(input())
colors = []
for n in range(N):
    colors.append(list(map(int, input().split())))
arr = [[0]*3 for _ in range(N)]

#현재 a 색을 고르면 그 전의 합에서 a 색이 아닌 값 중 작은 값을 더해주기
for i in range(N):
    if i == 0:
        arr[i] = colors[i]

    else:
        arr[i][0] = colors[i][0] + min(arr[i-1][1], arr[i-1][2])
        arr[i][1] = colors[i][1] + min(arr[i-1][0], arr[i-1][2])
        arr[i][2] = colors[i][2] + min(arr[i-1][0], arr[i-1][1])

# print(arr)
print(min(arr[n]))