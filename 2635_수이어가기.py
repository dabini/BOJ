num = int(input())
length = 0
for k in range(1, num+1):
    lst = [num, k]
    res = 100
    while True:
        res = lst[len(lst)-2] - lst[len(lst)-1]
        if res < 0:
            break
        lst.append(res)
    if len(lst) > length:
        length = len(lst)
        out = lst[:]
print(length)
print(*out)