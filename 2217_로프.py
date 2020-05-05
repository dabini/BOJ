import sys
input = sys.stdin.readline

minnum = 987654321
N = int(input())
for n in range(N):
    rope = int(input())
    if rope < minnum:
        minnum = rope
print(minnum*N)