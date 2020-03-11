N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())  # 총감독관이 감독할 수 있는 인원, 부감독관이 감독할 수 있는 인원
res = 0
for n in range(N):
    cnt = 0
    if A[n] > 0:
        A[n] -= B
        cnt = 1
    if A[n] > 0:
        cnt += int(A[n]/C)

        if A[n] % C:
            cnt +=1
    res += cnt
print(res)

