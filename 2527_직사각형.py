
for t in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2  = map(int, input().split())
    field = [[0] * 1000 for _ in range(1000)]
    res = 0
    for y in range(y1, q1+1):
        for x in range(x1, p1+1):
            field[y][x] += 1

    for j in range(y2, q2+1):
        for i in range(x2, p2+1):
            field[j][i] += 1

    checkx = [0]
    checky = [0]
    for b in range(q2+1):
        for a in range(q2+1):
            if field[b][a] == 2:
                res += 1

    if res == 0:
        ans = 'd'
    elif res == 1:
        ans = 'c'
    else:
        if x1 == x2 or x1 == p2 or p1 == x2 or p1 == q2 or y1 == y2 or y1 == q2 or q1 == y2 or q1 == q2:
            ans = 'b'
        else:
            ans = 'a'

    print(ans)

