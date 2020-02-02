#첫번째방법
# def d(n):
#     a = 0
#     for i in list(str(n)):
#         a = a+ int(i)
#     return int(n) + a
# a = []
# for i in range(1, 10001):
#     k = d(i)
#     a.append(k)
# for j in range(1, 10001):
#     if j in a:
#         pass
#     else:
#         print(j)

#두 번째 방법
# def d(n):
#     result = n
#     while n != 0:
#         result += n%10
#         n //10
#     return result
#
# lst = []
#
# for i in list(range(1, 10001)):
#     lst.append(d(i))
# for j in range(1, 10001):
#     if j not in lst:
#         print(j)

#세 번째 방법

number_set = set(range(1, 10001))
number_set2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    number_set2.add(i)

selfnumber_set = number_set - number_set2

for i in sorted(selfnumber_set):
    print(i)