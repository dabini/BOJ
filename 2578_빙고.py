# bingo = [[0]*5 for _ in range(5)]
#
# for i in range(5):
#     bingo[i] = list(map(int, input().split()))
#
# check = []
# for j in range(5):
#     check += list(map(int, input().split()))
#
# dx = [1, -1, 1, 0]
# dy = [1, 1, 0, 1]
# total = 0
#
# for k in range(len(check)):
#     for y in range(5):
#         for x in range(5):
#             if bingo[y][x] == check[k]:
#                 bingo[y][x] = 0
#
#     if k >= 14:
#         for a in range(4):
#             cnt = 0
#             for b in range(5):
#                 if bingo[b+(dx[a])][b+(dy[a])] == 0:
#                     cnt += 1
#                 else:
#                     break
#             if cnt == 5:
#                 total += 1
#         if total == 3:
#            break
# print(k)
#
