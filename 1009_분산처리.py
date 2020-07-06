import sys

input = sys.stdin.readline
T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    b = 4 + b % 4
    # 그냥 b %= 4 하면 0이 나올 수도 있기 때문에 오류 발생!!
    res = a**b%10
    if res == 0:
        res = 10
    print(res)