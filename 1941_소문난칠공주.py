"""
dfs활용하기..?
"""
import sys


def DFS(y, x):


input = sys.stdin.readline
arr = [list(input().strip()) for _ in range(5)]
# print(arr)
for y in range(5):
    for x in range(5):
        if arr[y][x] == 'Y':
            DFS(y, x)