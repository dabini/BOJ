# check = '666'
# lst = []
# for num in range(10000000):
#     if check in str(num):
#         lst.append(num)
#
# N = int(input())
# print(lst[N-1])

N,i=int(input()),9
while N:
 i+=1
 if '666' in str(i):
     N -= 1
print(i)