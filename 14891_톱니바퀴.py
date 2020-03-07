# def change(num, d):
#     tmp_arr = arr
#     for i in range(1, 4):
#         if arr[i][2] != arr[i+1][6]:
#             change_lst.append((i, i+1))
#
#     if (num-1, num) in change_lst:



arr = [[0]*8] +[list(map(int, input())) for _ in range(4)]
K = int(input()) #회전횟수
for k in range(K):
    num, d = map(int, input().split()) #바퀴번호, 방향(1이면 시계, -1이면 반시계)
    # change_lst = []
    # change(num, d)
    # print(change_lst)
    if d == 1:
        tmp = arr
        tmp[num] = [tmp[num].pop()] + [tmp_self]
        if num - 1 > 0 and arr[num][6] != arr[num-1][2]:
            tmp[num-1] = arr[num-1][:]
            tmp[num-1] = [tmp[num]] + [tmp[num].pop(0)]
        if num + 1 <= 4 and arr[num][2] != arr[num+1][6]:
            tmp_right = arr[num+1][:]
            tmp_right = [tmp_right] + [tmp_right.pop(0)]

    elif d == -1:
        tmp_self = arr[num][:]
        tmp_self = [tmp_self] + [tmp_self.pop(0)]
        if num - 1 > 0 and arr[num][6] != arr[num - 1][2]:
            tmp_left = arr[num - 1][:]
            tmp_left = [tmp_left.pop()] + [tmp_left]
        if num + 1 <= 4 and arr[num][2] != arr[num + 1][6]:
            tmp_right = arr[num + 1][:]
            tmp_right = [tmp_right] + [tmp_right.pop(0)]

    arr[num] = tmp_self
    if num-1 > 0 and arr[num][6] != arr[num - 1][2]:
        arr[num-1] = tmp_left
    if num + 1 <= 4 and arr[num][2] != arr[num + 1][6]:
        arr[num+1] = tmp_right


    # check_lst = [1, 2, 3, 4] - [num-1, num, num+1]
    # for c in check_lst:
    #     tmp_c = arr[c][:]
    #     if c - 1 > 0 and arr[c-1]:
    #         if arr[num][6] != arr[num - 1][2]:
    #             tmp_left = arr[num - 1][:]
    #             tmp_left = tmp_left.pop() + tmp_left
    #     if num + 1 <= 4:
    #         if arr[num][2] != arr[num + 1][6]:
    #             tmp_right = arr[num + 1][:]
    #             tmp_right = tmp_right + tmp_right.pop(0)

res = 0
for j in range(1, 5):
    if arr[j][0] == 1:
        res += 2**(j-1)
print(res)