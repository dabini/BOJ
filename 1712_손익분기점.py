A, B, C = map(int, input().split()) #A 고정비용 B 가변 비용 C 노트북 가격
k = 1
if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))