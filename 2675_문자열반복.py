T = int(input())

for t in range(T):
    R, S = map(str, input().split())
    R = int(R)
    S = list(S)
    out = ''
    for i in range(len(S)):
        out += S[i] *R
    print(out)