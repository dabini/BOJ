#캐슬디펜스
def shoot(s, tmp, N, M, D):
    minD = D + 1  # 최소 거리값 초기화
    ti, tj = -1, -1  # 화살을 맞는 적의 좌표 후보
    for i in range(N):
        for j in range(M):
            if tmp[i][j] > 0 and abs(i - N) + abs(j - s) <= D:  # 사거리 이내의 적이 있으면
                if minD > abs(i - N) + abs(j - s):
                    ti, tj = i, j
                    minD = abs(i - N) + abs(j - s)
                elif minD == abs(i - N) + abs(j - s) and j < tj:
                    ti, tj = i, j
                    minD = abs(i - N) + abs(j - s)
    if ti >= 0:  # 화살을 맞는 적이 있으면
        tmp[ti][tj] += 1  # 화살을 맞은 표시를 남김
    # 화살에 맞은 적을 센 후 지우고,

    # 적을 성벽쪽으로 이동


def defence(s1, s2, s3, N, M, D):
    tmp = [[0] * M for _ in range(N)]  # 게임판 선언
    for i in range(N):  # 초기 적의 배치를 복사해서 사용
        for j in range(M):
            tmp[i][j] = enemy[i][j]
    for _ in range(N):  # 게임의 turn, 가장 윗줄의 적까지 공격
        shoot(s1, tmp, N, M, D)  # tmp에서 화살을 맞은 적은 +1
        shoot(s2, tmp, N, M, D)
        shoot(s3, tmp, N, M, D)
        print()


N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]

# 궁수 배정
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            defence(i, j, k, N, M, D)


#캐슬디펜스_BFS
dr = [0, -1, 0] # 왼쪽, 위, 오른쪽
dc = [-1, 0, 1]

def shoot(aw, target, N, M, D): # aw가 맞추는 적을 target에 표시
    q = []
    v = [[0]*M for _ in range(N)] #이미 확인한 칸 표시
    q.append(N-1) # 궁수와 거리가 1인 칸은 바로 윗칸
    q.append(aw)
    v[N-1][aw] = 1
    while(len(q)!=0):
        r = q.pop(0)
        c = q.pop(0)

        if target[r][c]>0: # 만약 적이 있이면 가까운 순이므로 적을 맞추고 중지
            target[r][c] += 1
            return
        for k in range(3): # 왼쪽, 앞, 오른쪽 순으로 확인
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<M:
                if v[nr][nc] == 0 and v[r][c]<D: # 아직 확인안한 자리고 사거리 이내면
                    q.append(nr)
                    q.append(nc)
                    v[nr][nc] = v[r][c]+1

def shoot2(aw, target, N, M, D): # aw가 맞추는 적을 target에 표시
    minD = D+1
    ti, tj = -1, -1
    for i in range(N):
        for j in range(M):
            if target[i][j]>0 and abs(i-N)+abs(j-aw)<=D: # 사거리 단축
                if minD > abs(i-N)+abs(j-aw):
                    ti, tj = i, j
                    minD = abs(i-N)+abs(j-aw)
                elif abs(i-N)+abs(j-aw)==minD and j<tj: # 더 왼쪽
                    ti, tj = i, j
    if ti+tj>=0:
        target[ti][tj] += 1

def defence(aw1, aw2, aw3, N, M, D):
    target = [[0] * M for _ in range(N)]
    hit = 0
    for i in range(N):
        for j in range(M):
            target[i][j] = enemy[i][j]
    for i in range(N): # 사격 횟수
        # 궁수와 거리가 D이내에서 가장 가까운 적 중 맨 왼쪽의 적을 맞춤
        shoot2(aw1, target, N, M, D)
        shoot2(aw2, target, N, M, D)
        shoot2(aw3, target, N, M, D)
        for r in range(N): # 화살에 맞은 적을 가려냄
            for c in range(M):
                if target[r][c] > 1:
                    hit += 1
                    target[r][c] = 0
        for r in range(N-1, 0, -1):
            for c in range(M):
                target[r][c] = target[r-1][c] # 성벽쪽으로 이동
        for c in range(0, M):
            target[0][c] = 0 # 가장 외곽의 적은 성벽쪽으로 이동하고 없음
    return hit

N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(M-2): # 맨 왼쪽 궁수
    for j in range(i+1, M-1): # 가운데 궁수
        for k in range(j+1, M): # 오른쪽 궁수
            kill = defence(i, j, k, N, M, D)
            if maxV < kill:
                maxV = kill
print(maxV)