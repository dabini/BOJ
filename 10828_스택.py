import sys

N = int(input())
stack = []
n = 0
while n < N:
    order = sys.stdin.readline().rsplit()
    if order[0] == "push":
        stack += [int(order[1])]
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    elif order[0] == 'pop':
        if stack:
            p = stack.pop()
            print(p)
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    n += 1