import sys

input = sys.stdin.readline
n = int(input())
k = 1

while n > 0 :
    n -= k
    k += 1
if n <= 0:
    k -= 1
    n += k
# print(n)
# print(k)

if k%2:
    print("{}/{}".format(k-n+1, n))
else:
    print("{}/{}".format(n,k-n+1))