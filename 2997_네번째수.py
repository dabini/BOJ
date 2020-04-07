lst = sorted(list(map(int, input().split())))

a = lst[2] - lst[1]
b = lst[1] - lst[0]

if a == b:
    print(lst[2] + a)
elif a > b:
    print(lst[1] + b)
else:
    print(lst[0]+ a)