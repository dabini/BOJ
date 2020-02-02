alpha = list(input().upper())
lst = []
for i in range(len(alpha)):
    if alpha[i] not in lst:
        lst.append(alpha[i])
new = []
for i in range(len(lst)):
    cnt = alpha.count(lst[i])
    new.append(cnt)

max_num  = max(new)
if new.count(max_num) >1 :
    print('?')
else:
    print(alpha[new.index(max_num)])