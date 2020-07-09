import sys

input = sys.stdin.readline
M = int(input())
N = int(input())

res = 0
min_num = 987654321
for n in range(M, N+1):
    flag = True
    if n > 1:
        for k in range(2, n):
            if n%k==0:
                flag = False
                break
        if flag:
            res += n
            if n < min_num:
                min_num = n
if res:
    print(res)
    print(min_num)
else:
    print(-1)