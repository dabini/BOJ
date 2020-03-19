import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    word = str(sys.stdin.readline())
    if [len(word), word] not in lst:
        lst.append([len(word), word])
lst.sort()
for l in lst:
    print(l[1], end="")