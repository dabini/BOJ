import sys


input = sys.stdin.readline
n = int(input())
cnt_lst = [0, 1, 2]
if n > 2:
    for i in range(3, n+1):
        cnt_lst.append(cnt_lst[i-2] + cnt_lst[i-1])
print(cnt_lst[n]%10007)