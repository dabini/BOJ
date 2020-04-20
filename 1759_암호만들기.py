import sys
from itertools import combinations

input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
alphas = sorted(list(map(str, input().split())))

for alpha in combinations(alphas, L):
    cnt = 0
    for a in alpha:
        if a in vowels:
            cnt += 1
    if cnt >= 1 and L-cnt >= 2:
        print(''.join(alpha))