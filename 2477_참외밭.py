fruit_num = int(input())
lst = []

max_x = 0
max_y = 0

for _ in range(6):
    a, b = map(int, input().split())
    lst += [(a, b)]
# print(lst)

for l in lst:
    a, b = l
    if a == 1:
        if max_x < b:
            max_x = b
    elif a == 2:
        if max_x < b:
            max_x = b
    elif a == 3:
        if max_y < b:
            max_y = b
    else:
        if max_y < b:
            max_y = b

minus_x = 0
minus_y = 0

for j in range(len(lst)):
    a, b = lst[j]
    if a == 1 or a == 2:
        if b == max_x:
            minus_y = min(lst[j-1][1], lst[(j+1)%6][1])

    if a == 3 or a ==4:
        if b == max_y:
            minus_x = min(lst[j-1][1], lst[(j+1)%6][1])

res = max_y*max_x - minus_x*minus_y
print(fruit_num*res)


# n = int(input())
# value = [int(input().split()[1]) for _ in range(6)]
#
# idx = value.index(max(value))
# if value[idx-1] < value[(idx+1)%6]:
#     idx2 = (idx+1)%6
#     next = value[(idx+1)%6]
# else:
#     idx2 = idx -1
#     next = value[idx-1]
# print((next *value[idx] - value[idx-3]*value[idx2-3])*n)
