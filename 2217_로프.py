import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for n in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)
max_num = 0
for i in range(N):
    if ropes[i] * (i+1) > max_num:
        max_num = ropes[i] * (i+1)
print(max_num)