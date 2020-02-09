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