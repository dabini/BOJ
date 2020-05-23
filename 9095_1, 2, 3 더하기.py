import sys

input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    cnt_lst = [0, 1, 2, 4] # 각 수를 만들 수 있는 개수
    for i in range(4, n+1):
        cnt_lst.append(cnt_lst[i-1] + cnt_lst[i-2] + cnt_lst[i-3])
    print(cnt_lst[n])