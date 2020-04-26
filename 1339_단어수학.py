import sys
input = sys.stdin.readline


N = int(input())
num_lst = []
alphas = [0] * 26

for n in range(N):
    num_lst.append(input().strip())
# print(num_lst)

for num in num_lst:
    i = 0
    while num:
        now = num[-1]
        alphas[ord(now) - ord('A')] += 10**i
        i += 1
        num = num[:-1]

alphas.sort(reverse=True)
res = 0
for i in range(9, 0, -1):
    res += i * alphas[9-i]
print(res)