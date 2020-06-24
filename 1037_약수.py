import sys

input = sys.stdin.readline
N = int(input())
num_lst = list(map(int, input().split()))

print(max(num_lst) * min(num_lst))