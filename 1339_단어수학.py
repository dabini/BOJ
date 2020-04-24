"""
단어를 입력받을 때 단어의 길이 순으로 입력 받아서
단어 길이가 가장 긴 것부터 큰 숫자 만들기
다른 단어랑 숫자를 어떻게 일치시킬까?

"""
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