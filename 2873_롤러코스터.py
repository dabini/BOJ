R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
res = ""
if R%2:
    r = 0
    while r < R:
        if r%2:
            res += "L"*(C-1)
        else:
            res += "R"*(C-1)
        r += 1
        if r < R:
            res += "D"
else:

print(res)