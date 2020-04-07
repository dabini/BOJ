def check(N, M):
    if N % M == 0:
        return M
    return check(M, N%M)

N, M = map(int, input().split()) #소세지수, 평론가 수
print(M - check(N, M))
