import sys
input = sys.stdin.readline

def find(p, n):
    if n == N:
        return print(p)
    elif n < N:
        if p - volumes[n] >= 0:
            p -= volumes[n]
            find(p, n+1)
        elif p + volumes[n] <= M:
            p += volumes[n]
            find(p, n+1)
        else:
            return print(-1)

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))
find(S, 0)