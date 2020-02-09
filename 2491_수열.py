Num = int(input())
num_lst = list(map(int, input().split()))

max_cnt =1
out = []

#연속해서 커지는 것
cnt_increase = 1
for i in range(1, Num):
    if num_lst[i-1] <= num_lst[i]:
        cnt_increase += 1
    else:
        cnt_increase = 1
    if max_cnt < cnt_increase:
        max_cnt = cnt_increase

#연속해서 작아지는 것
cnt_decrease = 1
for i in range(1, Num):
    if num_lst[i-1] >= num_lst[i]:
        cnt_decrease += 1
    else:
        cnt_decrease = 1
    if max_cnt < cnt_decrease:
        max_cnt = cnt_decrease

print(max_cnt)