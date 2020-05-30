import sys

input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    order = list(input().split())
    # print(order)
    if len(order) > 1:
        q.append(int(order[1]))
    else:
        if order[0] == 'pop':
            if q:
                print(q.pop(0))
            else:
                print(-1)
        elif order[0] == 'size':
            print(len(q))
        elif order[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif order[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif order[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)