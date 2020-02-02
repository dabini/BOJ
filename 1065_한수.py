# def bj(n):
#     n = int(n)
#     cnt = 0
#     if n < 100:
#         return n
#     else:
#         for i in range(100, n+1):
#             a = (i//100)
#             b = ((i%100))//10
#             c = ((i%100))%10
#
#             if (a-b) == (b-c):
#                 cnt += 1
#         return cnt + 99

n = int(input())
cnt = 0
if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        a = (i//100)
        b = ((i%100))//10
        c = ((i%100))%10

        if (a-b) == (b-c):
            cnt += 1
    print(cnt+99)