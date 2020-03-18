w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

shark_x = (p + T) % (2 * w)
Y = (q + T) % (2*h)

if shark_x > w:
    x = w - (shark_x % w)
else:
    x = shark_x
if Y > h:
    y = h - (Y % h)
else:
    y = Y
print(x, y)

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
