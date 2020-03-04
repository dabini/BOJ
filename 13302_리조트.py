#
# 하루 이용권 10000원,
# 연손 3일 이용권 25000원 + 쿠폰 1장
# 연속 5일 이용권 37000원 + 쿠폰 2장
def resort(day, price):
    global min_price
    if day >= N:
        if price <= min_price:
            min_price = price
    else:

N, M = map(int, input().split())
days = [0] + [1] * (N)
no = list(map(int, input().split()))
for n in no:
    days[n] -= 1
print(days)
min_price = 10000 * (N-M) #모두 하루 이용권으로 이용

for day in days:
