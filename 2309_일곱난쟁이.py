lst = []
for i in range(9):
    h = int(input())
    lst.append(h)
lst = sorted(lst)
total = sum(lst)
for i in range(len(lst)):
    for j in range(i+ 1, len(lst)):
        if total - lst[i] - lst[j] == 100:
            for k in range(len(lst)):
                if i == k or j == k:
                    continue
                print(lst[k])
            exit(False)