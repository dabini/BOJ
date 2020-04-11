"""
항상 1,2,3 값에서 하나를 선택하게 설정하기
한자리수 증가할 때마다 좋은 수열인지 판단
=> 1자리수부터 길이//2 까지 대칭이 있는지 비교해보기
좋은 수열이면 자리수 +1 증가시키기
"""

import sys

def back(num, N):
    if N == 0:
        print("".join(list(map(str, num))))
        exit()
    else:
        for i in range(1,4):
            num.append(i)
            conf(num)
            if check:
                back(num, N-1)
            num.pop()

def conf(num):
    global check
    check = True
    for i in range(1, len(num)//2+1):
        for j in range(0, len(num)-i+1, i):
            if num[j:j+i] == num[j+i:j+i+i]:
                check = False
                return check

input = sys.stdin.readline
N = int(input())
num = [1]
back(num, N-1)