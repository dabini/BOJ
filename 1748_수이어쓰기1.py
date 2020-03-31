N = input()
length = len(N)
N = int(N)
res = 0
while N:
    tmp = N - (10 ** (length-1) ) + 1
    res += tmp * length
    N -= tmp
    length -= 1
    if N <= 0:
        break
print(res)
