"""
항상 1,2,3 값에서 하나를 선택하게 설정하기
한자리수 증가할 때마다 좋은 수열인지 판단
=> 1자리수부터 길이//2 까지 대칭이 있는지 비교해보기
좋은 수열이면 자리수 +1 증가시키기
"""

import sys
input = sys.stdin.readline

def solve(s, l):
    global check, res
    if check:
        return
    for i in range(1, l//2 + 1):
        a = int(s[l-i:])
        b = int(s[l-2*i:l-i])
        if a == b:
            return
    if l == n:
        res = s
        check = True
    for i in ['1', '2', '3']:
        solve(s+i, l+1)

n = int(input())
check = False
res = -1
solve('1', 1)
print(res)