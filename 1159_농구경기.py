N = int(input())

alpha= {}
for i in range(97, 123):
    alpha[chr(i)] = 0
# print(alpha)

for n in range(N):
    name = input()
    alpha[name[0]] += 1
# print(alpha)

res = []
for k, v in alpha.items():
    if v >= 5:
        res.append(k)

if res:
    print("".join(res))
else:
    print("PREDAJA")