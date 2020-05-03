import sys

input = sys.stdin.readline
price = int(input())
change = 1000 - price
money_list = [500, 100, 50, 10, 5, 1]
k = 0
res = 0
while change > 0 :
    if change >= money_list[k]:
        res += change // money_list[k]
        change = change % money_list[k]
    k += 1
print(res)