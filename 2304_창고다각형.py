N = int(input())
x_lst = []
lst= []


for n in range(N):
    L, H = map(int, input().split())
    x_lst += [L]
    lst += [[L, H]]

min_x = min(x_lst)
max_x = max(x_lst)
max_y = 0

data = [0]*(max_x+1)

for x in range(N):
    data[lst[x][0]] = lst[x][1]

idx_num = max(data)
idx = data.index(idx_num)

total = 0
max_y = 0
for k in range(max_x, idx, -1):
    if max_y < data[k]:
        max_y = data[k]
    total += max_y

max_y = 0
for j in range(1, idx+1):
    if max_y <data[j]:
        max_y = data[j]
    total += max_y
print(total)










