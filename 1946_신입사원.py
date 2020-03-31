import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    app = []
    for _ in range(n):
        document, interview = map(int, input().split())
        app.append([document, interview])
    app.sort()
    cnt = 1
    check = app[0][1]
    for a in range(1, n):
        if check > app[a][1]:
            cnt+= 1
            check = app[a][1]

    print(cnt)