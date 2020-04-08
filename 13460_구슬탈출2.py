"""
한 번에 한 방향에서 벽까지 이동 / 방향 바꿀 때마다 최소이동횟수 +1 하기
R이 B보다 O에 먼저 들어가야 성공! 이동횟수 출력
만약 R이 10번 이내로 O에 들어가지 못하거나 B가 먼저 들어갈 경우 -1 출력
#  #벽 . 이동가능한 통로?
필요한거.. q, visited,
"""
N, M = map(int, input().split())
game = [list(input()) for _ in range(N)]
# print(game)

for j in range(N):
    for i in range(M):
        if game[j][i] == 'R':
            ry, rx = j , i
        elif game[j][i] == "B":
            by, bx = j, i