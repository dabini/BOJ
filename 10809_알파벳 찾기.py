S = list(input())
lst = [0] * 26
check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(check)):
    if check[i] in S:
        lst[i] = str(S.index(check[i]))
    elif check[i] not in S:
        lst[i] = '-1'
print(" ".join(lst))