# def fibo(K):
#     if K <= 1:
#         return K
#     else:
#         return fibo(K-1) + fibo(K-2)
# K = int(input())
# print(fibo(K-1), end=" ")
# print(fibo(K))

import sys
input = sys.stdin.readline
K = int(input())
fibo = [0] * (K+1)
fibo[1] = 1

for i in range(2, K+1):
    fibo[i] = fibo[i-2] + fibo[i-1]
print(fibo[K-1], fibo[K])