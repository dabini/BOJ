import sys

input = sys.stdin.readline
a, b = map(int, input().split())
if a > b :
    bg = a
    sm = b
else:
    bg = b
    sm = a

for i in range(sm, 0, -1):
    if bg % i == 0 and sm % i == 0:
        res = i
        break

print(res)
print(bg*sm//res)