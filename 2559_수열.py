N, K = map(int, input().split()) #K는 연속날짜 N = 전체날짜

temp_lst = list(map(int, input().split()))

x = 0
total = sum(temp_lst[0:K])
max_sum = total

if K == 1:
    print(max(temp_lst))
else:
    while True:
        total -= temp_lst[x]
        if x +K >=N:
            break
        total += temp_lst[x+K]
        if max_sum < total:
            max_sum = total
        x += 1
    print(max_sum)

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
