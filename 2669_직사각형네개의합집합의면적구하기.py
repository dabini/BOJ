fieild =[[0]*100 for _ in range(100)]
cnt = 0
for k in range(4):
    lx, ly, rx, ry = map(int, input().split())

    for y in range(ly, ry):
        for x in range(lx, rx):
            fieild[y][x] +=1

for j in range(100):
    for i in range(100):
        if fieild[j][i] != 0:
            cnt +=1
print(cnt)