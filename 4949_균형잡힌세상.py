while True:
    check = input()
    if check == '.':
        break
    stack = [0]
    for c in check:
        res = 'yes'
        if c == '.':
            break
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
                continue
            else:
                res = 'no'
                break
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
                continue
            else:
                res = 'no'
                break

    if res == 'yes':
        if len(stack) > 1:
            res = 'no'
    print(res)