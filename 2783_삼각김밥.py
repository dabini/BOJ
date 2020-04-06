X, Y = map(int, input().split())
N = int(input())
price = X/Y * 1000
for n in range(N):
    x, y = map(int, input().split())
    tmp = x/y*1000
    if price > tmp:
        price = tmp
print("%.2f" %(price))