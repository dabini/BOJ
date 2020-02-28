N = int(input())
lst = []
for n in range(N):
    lst += [int(input())]

for i in sorted(lst):
    print(i)