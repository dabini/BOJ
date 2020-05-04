import sys
def fibo(n):
    for i in range(n+1):
        if i <= 1:
            res[i] = i
        else:
            res[i] = res[i-1] + res[i-2]


input = sys.stdin.readline
n = int(input())
res = [0 for _ in range(n+1)]
fibo(n)
print(res[n])