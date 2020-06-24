import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if  a == 0 and b == 0:
        break
    else:
        c = b // a
        d = a // b
        if b % a == 0 and a * c == b:
            print("factor")
        elif a % b == 0 and b * d == a:
            print("multiple")
        else:
            print("neither")

