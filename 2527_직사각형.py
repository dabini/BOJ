for t in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2  = map(int, input().split())
    Y = max(q1, q2)
    X = max(p1, p2)
    field = [[0] * (X+1) for _ in range(Y+1)]
    res = 0
    for y in range(y1, q1+1):
        for x in range(x1, p1+1):
            field[y][x] += 1

    for j in range(y2, q2+1):
        for i in range(x2, p2+1):
            field[j][i] += 1

    check = []
    for b in range(Y+1):
        for a in range(X+1):
            if field[b][a] == 2:
                res += 1
                check.append([a, b])

    if res == 0:
        ans = 'd'

    elif res == 1:
        ans = 'c'
    else:
        if check[0][1] == check[-1][1] or check[0][0] == check[-1][0]:
            ans = 'b'
        else:
            ans = 'a'
        # if x1 == x2 or x1 == p2 or p1 == x2 or p1 == p2 or y1 == y2 or y1 == q2 or q1 == y2 or q1 == q2:
        #     ans = 'b'
        # else:
        #     ans = 'a'
    print(ans)



for _ in range(4):
    i=list(map(int,input().split()))
    x=i[::2]
    y=i[1::2]
    a=len(set(range(x[0],x[1]+1)).intersection(set(range(x[2],x[3]+1))))
    b=len(set(range(y[0],y[1]+1)).intersection(set(range(y[2],y[3]+1))))
    if a>1 and b>1:
        print("a")
    elif (a==1 and b>1) or (a>1 and b==1):
        print("b")
    elif a==1 and b==1:
        print("c")
    else:
        print("d")