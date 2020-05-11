import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(N):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)