# N = int(input())
# num_lst = []
# for n in range(N):
#     num_lst.append(int(input()))
#
# for i in range(len(num_lst)-1):
#     swap = 0
#     for j in range(len(num_lst)-i-1):
#         if num_lst[j] > num_lst[j+1]:
#             num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
#             swap += 1
#     if swap == 0:
#         break
# for num in num_lst:
#     print(num)

import sys
N = int(input())
res = [0 for _ in range(10001)]
for n in range(N):
    a = int(sys.stdin.readline())
    res[a] += 1

for i in range(10001):
    if res[i] > 0:
        for j in range(res[i]):
            print(i)