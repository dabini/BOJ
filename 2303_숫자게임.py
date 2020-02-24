def permutation(lst, num): #lst는 순열을 구할 것, num은 순열의 개수
    global res
    used = [0 for _ in range(len(lst))] #중복값 제거를 위해 use 리스트 생성

    def generate(chosen, used):
        if len(chosen) == num:
            res.append(sum(chosen)%10)
            return

        for i in range(len(lst)):
            if not used[i]:
                chosen.append(lst[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

N = int(input())
ans = []
check = 0
result = 0
for n in range(N):
    res = []
    game_lst = list(map(int, input().split()))
    permutation(game_lst, 3)
    ans.append(max(res))

for n in range(N):
    if check <= ans[n]:
        check = ans[n]
        result = n+1
print(result)