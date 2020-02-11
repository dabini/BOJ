#1번 문제 풀이
# def check(cnt):
#     result = 0
#     result += bingo.count([0, 0, 0, 0, 0])
#     if result >= 3:
#         print(cnt)
#         return True
#     for i in range(5):
#         for j in range(5):
#             if bingo[j][i] != 0:
#                 break
#
#         else:
#             result += 1
#             if result >= 3:
#                 print(cnt)
#                 return  True
#     if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0 and bingo[3][3] == 0 and bingo[4][4] == 0:
#         result += 1
#         if result >=3:
#             print(cnt)
#             return True
#     if bingo[0][4] == 0 and bingo[1][3] == 0 and bingo[2][2] == 0 and bingo[3][1] == 0 and bingo[4][0] == 0:
#         result += 1
#         if result >= 3:
#             print(cnt)
#             return True
#     return False
#
# bingo = [input().split() for _ in range(5)]
# cnt = 0
# c = False
# for y in range(5):
#     for x in input().split():
#         cnt += 1
#         state = False
#         for j in range(5):
#             for k in range(5):
#                 if x == bingo[j][k]:
#                     state == True
#                     bingo[j][k] = 0
#                     c = check(cnt)
#                     break
#             if state:
#                 break
#         if c:
#             break
#     if c:
#         break

#2번 문제풀이
def bingo_x():
    res = 0
    for i in range(5):
        temp = True
        for j in range(5):
            if board[i*5+j]:
                temp = False
        if temp:
            res += 1
    return res


def bingo_y():
    res = 0
    for i in range(5):
        temp = True
        for j in range(5):
            if board[i+5*j]:
                temp = False
        if temp:
            res += 1
    return res


def bingo_z():
    res = 0
    temp = True
    for i in range(5):
        if board[i*6]:
            temp = False
    if temp:
        res += 1
    temp = True
    for i in range(1, 6):
        if board[i*4]:
            temp = False
    if temp:
        res += 1
    return res


board = []
for _ in range(5):
    board += input().split()
call = []
for _ in range(5):
    call += input().split()
for x in call:
    board[board.index(x)] = 0
    ans = bingo_x() + bingo_y() + bingo_z()
    if ans >= 3:
        break
print(call.index(x)+1)


