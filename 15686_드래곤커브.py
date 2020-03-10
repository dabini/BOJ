# '''
# 0세대 일때 1번 = 1
# 1세대 일 때 2의 0승 = 1 +1 =  2
# 2세대 2의 1승 = 2 + 1 + 1 = 4
# 3세대 2의 2승 = 4 + 2 + 1 + 1 = 8
# 4세대 2의 3승 = 8  + 4 + 2 + 1 + 1 = 16
# '''
#
# def check(d, g):
#     r = [d]
#     if g == 0:
#         return r
#     else:
#         for i in range(g):
#             for j in range(len(r)-1, -1, -1):
#                 r.append((r[j]+1)%4)
#     return r
#
# def find(x, y, c):
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
#     board[y][x] = 1
#     for d in c:
#         y = y + dy[d]
#         x = x + dx[d]
#         board[y][x] = 1
#
# N = int(input())
# board = [[0]* 101 for _ in range(101)]
# res = 0
# for n in range(N):
#     x, y, d, g = map(int, input().split())
#     find(x, y, check(d, g))
#
# for j in range(100):
#     for i in range(100):
#         if board[j][i] and board[j][i+1] and board[j+1][i] and board[j+1][i+1]:
#             res += 1
# print(res)

dx,dy=[1,0,-1,0],[0,-1,0,1]
def dc(y,x,d,g,k=-1,q=[]):
    if k==g:
        for i in q:
            b[i[0]][i[1]]=1
        return
    if k==-1:
        q.append((y,x))
        q.append((y+dy[d],x+dx[d]))
        dc(y+dy[d],x+dx[d],d,g,k+1,q)
    else:
        for i in range(len(q)):
            if q[i]!=(y,x):
                q.append((y-x+q[i][1],x+y-q[i][0]))
        dc(y-x+q[0][1],x+y-q[0][0],d,g,k+1,q)

n=int(input());ans=0
b=[[0]*101 for _ in 'a'*101]
for i in 'a'*n:
    x,y,d,g=map(int,input().split())
    dc(y,x,d,g,-1,[])
for i in range(100):
    for j in range(100):
        if b[i][j] and b[i+1][j] and b[i][j+1] and b[i+1][j+1]:ans+=1
print(ans)