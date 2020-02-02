C = int(input())

for c in range(C):
    lst = list(map(int, input().split()))
    num = lst[0]
    total = 0
    k = 0
    for i in range(1, len(lst)):
        total += lst[i]
    avg = total/num

    for j in range(1, len(lst)):
        if lst[j] > avg:
            k += 1
    print("%2.3f%%" % (k/num*100))