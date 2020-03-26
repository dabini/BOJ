import sys
input = sys.stdin.readline
def self(p, d):
    plane = check[p]
    if d == '+':
        plane[0][0], plane[2][0], plane[2][2], plane[0][2] = plane[2][0], plane[2][2], plane[0][2], plane[0][0]
        plane[0][1], plane[1][0], plane[2][1], plane[1][2] = plane[1][0], plane[2][1], plane[1][2], plane[0][1]
    elif d == '-':
        plane[0][0], plane[0][2], plane[2][2], plane[2][0] = plane[0][2], plane[2][2], plane[2][0], plane[0][0]
        plane[0][1], plane[1][2], plane[2][1], plane[1][0] = plane[1][2], plane[2][1], plane[1][0], plane[0][1]
    # temp = [[0]*3 for _ in range(3)]
    # if d == '+':
    #     for j in range(3):
    #         for i in range(3):
    #             temp[j][i] =  check[p][i][j]
    # elif d == '-':
    #     for j in range(3):
    #         for i in range(3):
    #             temp[j][i] = check[p][2-i][j]
    # check[p] = temp

def cube(p, d):
    if p == 'L':
        if d == '-':
            up[0][0], back[2][2], down[0][0], front[0][0] = front[0][0], up[0][0], back[2][2], down[0][0]
            up[1][0], back[1][2], down[1][0], front[1][0] = front[1][0], up[1][0], back[1][2], down[1][0]
            up[2][0], back[0][2], down[2][0], front[2][0] = front[2][0], up[2][0], back[0][2], down[2][0]
        elif d == '+':
            up[0][0], front[0][0], down[0][0], back[2][2] = back[2][2], up[0][0], front[0][0], down[0][0]
            up[1][0], front[1][0], down[1][0], back[1][2] = back[1][2], up[1][0], front[1][0], down[1][0]
            up[2][0], front[2][0], down[2][0], back[0][2] = back[0][2], up[2][0], front[2][0], down[2][0]
    elif p == 'R':
        if d == '+':
            up[0][2], back[2][0], down[0][2], front[0][2] = front[0][2], up[0][2], back[2][0], down[0][2]
            up[1][2], back[1][0], down[1][2], front[1][2] = front[1][2], up[1][2], back[1][0], down[1][2]
            up[2][2], back[0][0], down[2][2], front[2][2] = front[2][2], up[2][2], back[0][0], down[2][2]
        elif d == '-':
            up[0][2], front[0][2], down[0][2], back[2][0] = back[2][0], up[0][2], front[0][2], down[0][2]
            up[1][2], front[1][2], down[1][2], back[1][0] = back[1][0], up[1][2], front[1][2], down[1][2]
            up[2][2], front[2][2], down[2][2], back[0][0] = back[0][0], up[2][2], front[2][2], down[2][2]
    elif p == 'F':
        if d == '-':
            up[2][0], left[2][2], down[0][2], right[0][0] = right[0][0], up[2][0], left[2][2], down[0][2]
            up[2][1], left[2][1], down[0][1], right[1][0] = right[1][0], up[2][1], left[1][2], down[0][1]
            up[2][2], left[2][0], down[0][0], right[2][0] = right[2][0], up[2][2], left[0][2], down[0][0]
        elif d == '+':
            up[2][0], right[0][0], down[0][2], left[2][2] = left[2][2], up[2][0], right[0][0], down[0][2]
            up[2][1], right[1][0], down[0][1], left[1][2] = left[1][2], up[2][1], right[1][0], down[0][1]
            up[2][2], right[2][0], down[0][0], left[0][2] = left[0][2], up[2][2], right[2][0], down[0][0]
    elif p == 'B':
        if d == '+':
            up[0][0], left[0][0], down[2][0], right[2][2] = right[2][2], up[0][0], left[0][0], down[2][0]
            up[0][1], left[1][0], down[2][1], right[1][2] = right[1][2], up[0][1], left[1][0], down[2][1]
            up[0][2], left[2][0], down[2][2], right[0][2] = right[0][2], up[0][2], left[2][0], down[2][2]
        elif d == '-':
            up[0][2], right[2][2], down[2][0], left[0][0] = left[0][0], up[0][2], right[2][2], down[2][0]
            up[0][1], right[1][2], down[2][1], left[1][0] = left[1][0], up[0][1], right[1][2], down[2][1]
            up[0][0], right[0][2], down[2][2], left[2][0] = left[2][0], up[0][0], right[0][2], down[2][2]
    elif p == 'U':
        if d == '-':
            front[0][0], right[0][0], back[0][0], left[0][0] = left[0][0], front[0][0], right[0][0], back[0][0]
            front[0][1], right[0][1], back[0][1], left[0][1] = left[0][1], front[0][1], right[0][1], back[0][1]
            front[0][2], right[0][2], back[0][2], left[0][2] = left[0][2], front[0][2], right[0][2], back[0][2]
        elif d == '+':
            front[0][0], left[0][0], back[0][0], right[0][0] = right[0][0], front[0][0], left[0][0], back[0][0]
            front[0][1], left[0][1], back[0][1], right[0][1] = right[0][1], front[0][1], left[0][1], back[0][1]
            front[0][2], left[0][2], back[0][2], right[0][2] = right[0][2], front[0][2], left[0][2], back[0][2]
    elif p == 'D':
        if d == '+':
            front[2][0], right[2][0], back[2][0], left[2][0] = left[2][0], front[2][0], right[2][0], back[2][0]
            front[2][1], right[2][1], back[2][1], left[2][1] = left[2][1], front[2][1], right[2][1], back[2][1]
            front[2][2], right[2][2], back[2][2], left[2][2] = left[2][2], front[2][2], right[2][2], back[2][2]
        elif d == '-':
            front[2][0], left[2][0], back[2][0], right[2][0] = right[2][0], front[2][0], left[2][0], back[2][0]
            front[2][1], left[2][1], back[2][1], right[2][1] = right[2][1], front[2][1], left[2][1], back[2][1]
            front[2][2], left[2][2], back[2][2], right[2][2] = right[2][2], front[2][2], left[2][2], back[2][2]
# def cube(p, d):
#     self(p, d)
#     if p == 'L':
#         tmp = []
#         if d == '+':
#             for i in range(3):
#                 tmp.append(up[i][0])
#                 up[i][0] = back[i][2]
#                 back[i][2] = down[i][0]
#                 down[i][0] = front[i][0]
#             for i in range(3):
#                 front[i][0] = tmp[i]
#         elif d == '-':
#             for i in range(3):
#                 tmp.append(up[i][0])
#                 up[i][0] = front[i][0]
#                 front[i][0] = down[i][0]
#                 down[i][0] = back[i][2]
#             for i in range(3):
#                 back[i][2] = tmp[i]
#     elif p == 'R':
#         tmp = []
#         if d == '-':
#             for i in range(3):
#                 tmp.append(up[i][2])
#                 up[i][2] = back[i][2]
#                 back[i][2] = down[i][2]
#                 down[i][2] = front[i][2]
#             for i in range(3):
#                 front[i][2] = tmp[i]
#         elif d == '+':
#             for i in range(3):
#                 tmp.append(up[i][2])
#                 up[i][2] = front[i][2]
#                 front[i][2] = down[i][2]
#                 down[i][2] = back[0][2-i]
#             for i in range(3):
#                 back[0][2-i] = tmp[i]
#     elif p == 'F':
#         tmp = []
#         if d == '+':
#             for i in range(3):
#                 tmp.append(up[2][i])
#                 up[2][i] = left[i][2]
#                 left[i][2] = down[2][i]
#                 down[2][i] = right[0][i]
#             for i in range(3):
#                 right[0][i] = tmp[i]
#         elif d == '-':
#             for i in range(3):
#                 tmp.append(up[2][i])
#                 up[2][i] = right[i][0]
#                 right[i][0] = down[2][i]
#                 down[2][i] = left[i][2]
#             for i in range(3):
#                 left[i][2] = tmp[i]
#     elif p == 'B':
#         tmp = []
#         if d == '-':
#             for i in range(3):
#                 tmp.append(up[0][i])
#                 up[0][i] = left[i][0]
#                 left[i][0] = down[0][i]
#                 down[0][i] = right[i][2]
#             for i in range(3):
#                 right[i][2] = tmp[i]
#         elif d == '+':
#             for i in range(3):
#                 tmp.append(up[0][i])
#                 up[0][i] = right[i][2]
#                 right[i][2] = down[0][i]
#                 down[0][i] = left[i][0]
#             for i in range(3):
#                 left[i][0] = tmp[i]
#     elif p == 'T':
#         tmp = []
#         if d == '+':
#             for i in range(3):
#                 tmp.append(back[0][i])
#                 back[0][i] = left[0][i]
#                 left[0][i] = front[0][i]
#                 front[0][i] = right[0][i]
#             for i in range(3):
#                 right[0][i] = tmp[i]
#         elif d == '-':
#             for i in range(3):
#                 tmp.append(back[0][i])
#                 back[0][i] = right[0][i]
#                 right[0][i] = front[0][i]
#                 front[0][i] = left[0][i]
#             for i in range(3):
#                 left[0][i] = tmp[i]
#     elif p == 'D':
#         tmp = []
#         if d == '-':
#             for i in range(3):
#                 tmp.append(back[2][i])
#                 back[2][i] = left[2][i]
#                 left[2][i] = front[2][i]
#                 front[2][i] = right[2][i]
#             for i in range(3):
#                 right[2][i] = tmp[i]
#         elif d == '+':
#             for i in range(3):
#                 tmp.append(back[2][i])
#                 back[2][i]= left[2][i]
#                 left[2][i] = front[2][i]
#                 front[2][i] = right[2][i]
#             for i in range(3):
#                 right[2][i] = tmp[i]

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(str, input().split()))
    up = [['w']*3 for _ in range(3)]
    down = [['y']*3 for _ in range(3)]
    left = [['g']*3 for _ in range(3)]
    right = [['b']*3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    check = {'U': up, 'D': down, 'L': left, 'R': right, 'F': front, 'B': back }
    for i in range(n):
        p = lst[i][0] #돌린면
        d = lst[i][1] #방향
        cube(p, d)
        self(p, d)
    for j in range(3):
        print(''.join(up[j]))


# def self(array, d):
#     if d == '-':    # 반시계방향
#         array[0][0], array[0][2], array[2][2], array[2][0] = array[0][2], array[2][2], array[2][0], array[0][0]
#         array[0][1], array[1][2], array[2][1], array[1][0] = array[1][2], array[2][1], array[1][0], array[0][1]
#     elif d == '+':  # 시계방향
#         array[0][0], array[2][0], array[2][2], array[0][2] = array[2][0], array[2][2], array[0][2], array[0][0]
#         array[0][1], array[1][0], array[2][1], array[1][2] = array[1][0], array[2][1], array[1][2], array[0][1]
#
# def cube(p, d):
#     if p == 'L':
#         if d == '-':
#             up[0][0], back[2][2], down[0][0], front[0][0] = front[0][0], up[0][0], back[2][2], down[0][0]
#             up[1][0], back[1][2], down[1][0], front[1][0] = front[1][0], up[1][0], back[1][2], down[1][0]
#             up[2][0], back[0][2], down[2][0], front[2][0] = front[2][0], up[2][0], back[0][2], down[2][0]
#         elif d == '+':
#             up[0][0], front[0][0], down[0][0], back[2][2] = back[2][2], up[0][0], front[0][0], down[0][0]
#             up[1][0], front[1][0], down[1][0], back[1][2] = back[1][2], up[1][0], front[1][0], down[1][0]
#             up[2][0], front[2][0], down[2][0], back[0][2] = back[0][2], up[2][0], front[2][0], down[2][0]
#     elif p == 'R':
#         if d == '+':
#             up[0][2], back[2][0], down[0][2], front[0][2] = front[0][2], up[0][2], back[2][0], down[0][2]
#             up[1][2], back[1][0], down[1][2], front[1][2] = front[1][2], up[1][2], back[1][0], down[1][2]
#             up[2][2], back[0][0], down[2][2], front[2][2] = front[2][2], up[2][2], back[0][0], down[2][2]
#         elif d == '-':
#             up[0][2], front[0][2], down[0][2], back[2][0] = back[2][0], up[0][2], front[0][2], down[0][2]
#             up[1][2], front[1][2], down[1][2], back[1][0] = back[1][0], up[1][2], front[1][2], down[1][2]
#             up[2][2], front[2][2], down[2][2], back[0][0] = back[0][0], up[2][2], front[2][2], down[2][2]
#     elif p == 'F':
#         if d == '-':
#             up[2][0], left[2][2], down[0][2], right[0][0] = right[0][0], up[2][0], left[2][2], down[0][2]
#             up[2][1], left[2][1], down[0][1], right[1][0] = right[1][0], up[2][1], left[1][2], down[0][1]
#             up[2][2], left[2][0], down[0][0], right[2][0] = right[2][0], up[2][2], left[0][2], down[0][0]
#         elif d == '+':
#             up[2][0], right[0][0], down[0][2], left[2][2] = left[2][2], up[2][0], right[0][0], down[0][2]
#             up[2][1], right[1][0], down[0][1], left[1][2] = left[1][2], up[2][1], right[1][0], down[0][1]
#             up[2][2], right[2][0], down[0][0], left[0][2] = left[0][2], up[2][2], right[2][0], down[0][0]
#     elif p == 'B':
#         if d == '+':
#             up[0][0], left[0][0], down[2][0], right[2][2] = right[2][2], up[0][0], left[0][0], down[2][0]
#             up[0][1], left[1][0], down[2][1], right[1][2] = right[1][2], up[0][1], left[1][0], down[2][1]
#             up[0][2], left[2][0], down[2][2], right[0][2] = right[0][2], up[0][2], left[2][0], down[2][2]
#         elif d == '-':
#             up[0][2], right[2][2], down[2][0], left[0][0] = left[0][0], up[0][2], right[2][2], down[2][0]
#             up[0][1], right[1][2], down[2][1], left[1][0] = left[1][0], up[0][1], right[1][2], down[2][1]
#             up[0][0], right[0][2], down[2][2], left[2][0] = left[2][0], up[0][0], right[0][2], down[2][2]
#     elif p == 'U':
#         if d == '-':
#             front[0][0], right[0][0], back[0][0], left[0][0] = left[0][0], front[0][0], right[0][0], back[0][0]
#             front[0][1], right[0][1], back[0][1], left[0][1] = left[0][1], front[0][1], right[0][1], back[0][1]
#             front[0][2], right[0][2], back[0][2], left[0][2] = left[0][2], front[0][2], right[0][2], back[0][2]
#         elif d == '+':
#             front[0][0], left[0][0], back[0][0], right[0][0] = right[0][0], front[0][0], left[0][0], back[0][0]
#             front[0][1], left[0][1], back[0][1], right[0][1] = right[0][1], front[0][1], left[0][1], back[0][1]
#             front[0][2], left[0][2], back[0][2], right[0][2] = right[0][2], front[0][2], left[0][2], back[0][2]
#     elif p == 'D':
#         if d == '+':
#             front[2][0], right[2][0], back[2][0], left[2][0] = left[2][0], front[2][0], right[2][0], back[2][0]
#             front[2][1], right[2][1], back[2][1], left[2][1] = left[2][1], front[2][1], right[2][1], back[2][1]
#             front[2][2], right[2][2], back[2][2], left[2][2] = left[2][2], front[2][2], right[2][2], back[2][2]
#         elif d == '-':
#             front[2][0], left[2][0], back[2][0], right[2][0] = right[2][0], front[2][0], left[2][0], back[2][0]
#             front[2][1], left[2][1], back[2][1], right[2][1] = right[2][1], front[2][1], left[2][1], back[2][1]
#             front[2][2], left[2][2], back[2][2], right[2][2] = right[2][2], front[2][2], left[2][2], back[2][2]

# N = int(input())
# for _ in range(N):
#     M = int(input())
#     dt = {
#     'U' : [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], #윗면
#     'D' : [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], #아랫면
#     'F' : [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], #앞면
#     'B' : [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], #뒷면
#     'L' : [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], #왼쪽면
#     'R' : [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], #오른쪽면
#     }
#     for x in input().split():
#         side, direction = x[0], x[1]
#         cube(side, direction)          # 옆 면 회전
#         self(dt[side], direction)     # 해당 면 회전
#     for i in dt['U']:
#         print(''.join(i))
