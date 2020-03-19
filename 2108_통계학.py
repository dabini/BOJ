from collections import Counter
import sys

def mean(lst):
    return round(sum(lst)/N)
def median(lst):
    lst.sort()
    if N ==1:
        return lst[0]
    else:
        if N % 2:
            return lst[N//2]
        else:
            return round((lst[N//2] + lst[N//2 +1])/2)
def mode(lst):
    if n == 1:
        return lst[0]
    else:
        c = Counter(lst).most_common(2)
        if c[0][1] == c[1][1]:
            return c[1][0]
        else:
            return c[0][0]

def diff(lst):
    return max(lst) - min(lst)
N = int(sys.stdin.readline())
lst = []
for n in range(N):
    lst.append(int(sys.stdin.readline()))

print(mean(lst))
print(median(lst))
print(mode(lst))
print(diff(lst))

import sys
from collections import Counter

# main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))


def mean(nums):
    return round(sum(nums) / len(nums))


def median(nums):
    nums.sort()
    mid = nums[len(nums) // 2]  # nums의 개수는 홀수

    return mid


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


def scope(nums):
    return max(nums) - min(nums)


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))