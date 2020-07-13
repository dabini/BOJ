import sys

x_list = []
y_list = []
input = sys.stdin.readline
for _ in range(3):
    x, y = map(int, input().split())
    if x not in x_list:
        x_list.append(x)
    else:
        x_list.remove(x)
    if y not in y_list:
        y_list.append(y)
    else:
        y_list.remove(y)

print("{} {}".format(x_list[0], y_list[0]))