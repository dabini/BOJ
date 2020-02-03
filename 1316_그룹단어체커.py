N = int(input())
lst = []
for n in range(N):
    inp = list(input())

    for i in range(len(inp)):
        if i != len(inp)- 1 and inp[i] == inp[i+1]:
            pass
        elif inp[i+1:].count(inp[i]) != 0:
            break
        elif i == len(inp) -1:
            lst.append(i)
print(len(lst))