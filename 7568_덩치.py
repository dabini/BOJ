T = int(input())
lst = [[0] * 2 for _ in range(T)]
ans = []
for t in range(T):
    lst[t] = list(map(int, input().split()))

for i in lst:
    res = 1

    for j in lst:
        if (i[0] != j[0]) and (i[1] != j[1]):
            if ((i[0] < j[0])) and (i[1] < j[1]):
                res +=1
    ans.append(res)
print(*ans)
