import sys


input = sys.stdin.readline
n = int(input())
stair_lst = [0]
for n in range(n):
    stair_lst.append(int(input()))

score = [[0, 0] for _ in range(n+2)]

for i in range(1, n+2):
    if i == 1:
        score[1][0] = stair_lst[1]
    elif i ==2:
        score[2][0] = stair_lst[1] + stair_lst[2]
    else:
        score[i][0] = max(score[i-3]) + stair_lst[i-1] + stair_lst[i]
        score[i][1] = max(score[i-2]) + stair_lst[i]
# print(stair_lst)
# print(score)
print(max(score[n+1]))

