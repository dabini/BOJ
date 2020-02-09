A, B, V = map(int, input().split())
cnt = (V-B) / (A-B)
if cnt % 1 > 0:
    print(int(cnt)+1)
else:
    print(int(cnt))