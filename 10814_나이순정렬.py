import sys
lst = []
for i in range(int(sys.stdin.readline())):
    age, name = map(str, sys.stdin.readline().split())
    lst.append([int(age), i, name])
lst.sort()
for l in lst:
    print(l[0], l[2])