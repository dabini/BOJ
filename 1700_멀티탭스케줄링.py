import sys

N, K = map(int, input().split())
plugs = dict()
for i in range(1, K+1):
    plugs[i] = 0
lst = list(map(int, input().split()))
for l in lst:
    plugs[l] += 1
# print(plugs)

check = [0 for _ in range(N)]
