max_y, max_x = map(int, input().split())

cut_num = int(input())
x_lst = [0, max_x]
y_lst = [0, max_y]
for cut in range(cut_num):
    a, b = map(int, input().split())
    if a == 0:
        x_lst += [b]
    elif a ==1:
        y_lst += [b]

x_lst.sort()
y_lst.sort()

# print(*x_lst)
# print(*y_lst)

out = []
for j in range(1, len(y_lst)):
    for i in range(1, len(x_lst)):
        out += [(y_lst[j] - y_lst[j-1]) * (x_lst[i] - x_lst[i-1])]
print(max(out))
