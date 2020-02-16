Y, X = map(int, input().split())
cheese = [[0]*X for _ in range(Y)]

for i in range(Y):
    cheese[i] = list(map(int, input().split()))

if