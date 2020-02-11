w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

# xd = 1
# yd = 1
# while T > 0:
#     if 0 <= p <= w and 0 <= q <= h:
#         if p == 0 or p == w:
#             xd = -xd
#         elif q ==0 or q == h:
#             yd = -xd
#         p = p + xd
#         q = q + yd
#         T -= 1
# print(p, q)

if p + T <= w:
    x = p+T
else:
    if (p+T) % (2*w) > w:
        x = w - ((p+T) % w)
    else:
        x = (p+T) % w
if q + T <= h:
    y = q+T
else:
    if (q+T) % (2*h) > h:
        y = h - ((q+T) % h)
    else:
        y = (q+T) % h
print(x, y)