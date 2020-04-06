n = 1
res = 0
lst = []
scores = []
for _ in range(8):
    scores.append([int(input()), n])
    n += 1
scores.sort()
scores = scores[::-1]
for i in range(5):
    res += scores[i][0]
    lst.append(scores[i][1])
print(res)
print(*sorted(lst))