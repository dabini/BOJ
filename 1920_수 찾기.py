"""
이분 탐색으로 문제 해결
이분 탐색 조건
1. 이분 탐색하려는 배열이 이미 정렬되어 있어야 한다.
2. left, right 값을 활용해 mid값을 잡아준다.
3. mid값을 통해 구하려 하는 값과 비교해준다.
4. 비교할시 mid값보다 구하고자 하는 값이 크면 left를 mid+1로 만들어주고 작을 경우엔 rigjt를 mid -1로 만들어준다.
5. left > right 될 때까지 while 문을 반복한다.

"""
import sys

def find(num):
    global res
    left = 0
    right = N -1
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if n_lst[mid] == num:
            res = 1
            break
        elif n_lst[mid] > num:
            right = mid -1
        elif n_lst[mid] < num:
            left = mid + 1

input = sys.stdin.readline
N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
M = int(input())
m_lst = list(map(int, input().split()))

for m in m_lst:
    find(m)
    print(res)