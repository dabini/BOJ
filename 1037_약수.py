import sys

input = sys.stdin.readline
N = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

print(num_lst[0] * num_lst[-1])
