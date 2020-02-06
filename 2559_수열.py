N, K = map(int, input().split()) #K는 연속날짜 N = 전체날짜

temp_lst = list(map(int, input().split()))
res = -100

for n in range(0, N-K+1):
    if res < n:
        res = n




    # temp = temp_lst[n:n+K]
    #
    #
    # print(temp)

#     if res < temp:
#         res = temp
# print(res)