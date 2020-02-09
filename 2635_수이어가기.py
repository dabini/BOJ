<<<<<<< HEAD
N = int(input())
max_l = 0
max_list = []
for i in range(N+1):
    res = [N, i]
    j = 0
    while(True):
        a = res[j] = res[j+1]
        if a <= -1:
            break
        res.append(a)
        if max_l < len(res):
            max_l = len(res)
            max_list = res[:]
        j += 1
print(max_l)
for k in max_list:
    print(k, end=" ")
print()
=======
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
>>>>>>> e81a8dd71b025135508ece9b0e46853dbe02b6dd
