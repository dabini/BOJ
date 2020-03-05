from itertools import combinations

def find(chain, home):
    ans = 0
    for h in home:
        min_num = 987654321
        for c in chain:
            d = abs(c[0] - h[0]) + abs(c[1] - h[1])
            min_num = min(min_num, d)
        ans += min_num
    return ans

N, M = map(int, input().split())  #도시 크기, 치킨집 수
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []

for j in range(N):
    for i in range(N):
        if city[j][i] == 2:
            chicken.append((i, j))
        elif city[j][i] == 1:
            home.append((i, j))

chain = list(combinations(chicken, M))


min_res = 3987654321
for c in chain:
    res = find(list(c), home)
    min_res = min(min_res, res)

print(min_res)