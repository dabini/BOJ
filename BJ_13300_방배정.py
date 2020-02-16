# stu_num, max_num = map(int, input().split())
# lst = [[0, 0] for stu in range(6)]
# # lst = []
# # for stu in range(stu_num):
# #     lst.append([0,0])
#
# for stu in range(stu_num):
#     sex, grade = map(int, input().split())
#     lst[grade-1][sex] += 1
#
# cnt = 0
# for i in lst:
#     for j in i:
#         cnt += ( j + (max_num - 1)) // max_num
#         #-1하는 이유는 올림하기 위해
# print(cnt)

num, max_num = map(int, input().split())
lst = [[0, 0] for _ in range(6)]

for n in range(num):
    s, g = map(int, input().split())
    lst[g-1][s] += 1

cnt = 0
for i in lst:
    for j in i:
        cnt += ( j+ (max_num-1)) //max_num
print(cnt)