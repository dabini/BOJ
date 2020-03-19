# import sys
# N = int(sys.stdin.readline())
# chess = [[0]*N for _ in range(N)]
#
# visitedX = [0] * (N+1)
# visitedIncrease = [0] * (2*N+1)
# visitedDecrease = [0] * (2*N+1)
#
# def GetSome(y):
#     global ans
#     if y > N:
#         ans += 1
#         return
#     for x in range(1, N+1):
#         if not visitedX[x] and not visitedIncrease[y+x] and not visitedDecrease[y-x+4]:
#             visitedX[x] = visitedIncrease[y+x] = visitedDecrease[y-x+4] = 1
#             GetSome(y+1)
#             visitedX[x] = visitedIncrease[y+x] = visitedDecrease[y-x+4] = 0
# ans = 0
# GetSome(1)
# print(ans)

n=int(input())
count=0
row,left,right=[0 for _ in range(n)],[0 for _ in range(2*n-1)],[0 for _ in range(2*n-1)]
#수직,왼쪽대각선,오른쪽 대각선

def backtracking(index):
    global count

    if index==n:    #끝까지 퀸을 넣으면
        count+=1
        return

    for col in range(n):  #열을 이동하며
        if row[col] + left[index+col] + right[n-1+index-col]==0: #세조건에 걸리지 않는다면
            row[col]=left[index+col]=right[n-1+index-col]=1
            backtracking(index+1)
            row[col]= left[index+col]= right[n-1+index-col] = 0#초기화

backtracking(0)

print(count)

