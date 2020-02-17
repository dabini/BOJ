T = int(input())

for t in range(T):
    stack = []
    res = "YES"
    check = input()
    for c in check:
        if c == '(':
            stack += [c]
        else:
            if stack:
                stack.pop()
            else:
                res = "NO"
    if res != "NO":
        if stack:
            res = "NO"
        else:
            res = 'YES'
    print(res)