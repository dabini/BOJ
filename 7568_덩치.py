T = int(input())
lst = [[0] * 2 for _ in range(T)]

for t in range(T):
    lst[t] = list(map(int, input().split()))
print(lst)
res = [0] * T
a = 1
