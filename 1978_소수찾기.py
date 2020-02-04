N = int(input())
lst = list(map(int, input().split()))

k = 0
for i in lst:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt +=1
    if cnt == 2:
        k +=1
print(k)