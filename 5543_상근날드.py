import sys

input = sys.stdin.readline

burger = 2000
beverage = 2000
for _ in range(3):
    price = int(input())
    if burger >= price:
        burger = price

for _ in range(2):
    price = int(input())
    if beverage >= price:
        beverage = price

print(burger + beverage - 50)