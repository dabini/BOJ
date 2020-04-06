from itertools import combinations

lst = []
for n in range(9):
    lst.append(int(input()))

c = combinations(lst, 7)
for i in list(c):
    if sum(i) == 100:
        res = i
for a in res:
    print(a)