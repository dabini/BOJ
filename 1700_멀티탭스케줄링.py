"""
1. 멀티탭이 비어있을 경우 지금 사용할 기기를 꽂음. (set에 넣음)

2. 지금 사용할 기기가 이미 멀티탭에 꽂혀있는 경우, 그냥 넘어갑니다. (continue)

3. 1,2번이 둘다 아닐경우

3-1. 꽂혀있는 모든 기기가 나중에 다시 사용될 경우, 제일 나중에 사용될 기기를 찾아서 빼고, 지금 사용할 기기를 꽂음.(플러그 빼는 횟수 +1)

3-2. 꽂혀있는 기기중에 나중에 다시 사용되지 않는 기기가 있을 경우, 그 중에서 아무거나 하나 빼고, 지금 사용할 기기를 꽂음.(플러그 빼는 횟수 +1)
"""


import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().split()))
check = []
res = 0

for i in range(K):
    max_idx = 0
    if lst[i] not in check:
        if len(check) < N:
            check.append(lst[i])
            lst[i] = 0
        else:
            for c in range(N):
                if lst.count(check[c]) == 0:
                    d = check[c]
                    break
                else:
                    if max_idx < lst.index(check[c]):
                        max_idx = lst.index(check[c])
                        d = lst[max_idx]
            check.remove(d)
            res += 1
            check.append(lst[i])
            lst[i] = 0

    else:
        lst[i] = 0
        continue
print(res)