di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def find(v):
    q = [v]
    block[v[0]][v[1]] = 0
    level = 0
    result = 0
    while q:
        level += 1
        for _ in range(len(q)):
            v = q.pop(0)
            for a in range(4):
                if block[v[0] + di[a]][v[1]+dj[a]]:
                    if block[v[0] +di[a]][v[1]+dj[a]] ==2:
                        result += level
                    block[v[0]+di[a]][v[1]+dj[a]] =0
                    q.append([v[0]+di[a], v[1]+dj[a]])
    return result

w, h = map(int, input().split())
block = [[0] *(w+3)] + [[0]+[1]*(w+1)+[0]] + [[0]+[1]+[0]*(w-1)+[1]+[0] for _ in range(h-1)] +[[0]+[1]*(w+1)+[0]] + [[0]*(w+3)]
N = int(input())
for i in range(N):
    data = list(map(int, input().split()))
    if data[0] ==1:
        block[h+1][1+data[1]] =2
    elif data[0] ==2:
        block[1][1+data[1]] =2
    elif data[0] ==3:
        block[h+1-data[1]][1] =2
    elif data[0] ==4:
        block[h+1-data[1]][w+1] =2
start = list(map(int, input().split()))
if start[0] ==1:
    start = [h+1, 1+start[1]]
elif start[0] ==2:
    start = [1, 1+start[1]]
elif start[0] ==3:
    start = [h+1-start[1],1]
elif start[0] ==4:
    start = [h+1-start[1], w+1]
print(find(start))


#두번째
xn, yn = map(int, input().split())
n = int(input())

store = [0] * n
for i in range(n):
    store[i] = list(map(int, input().split()))
car = list(map(int, input().split()))

sum = 0
for i in range(n):
    if store[i][0] == car[0]:
        sum += abs(store[i][1] - car[1])
    elif store[i][0] + car[0] == 3:
        if store[i][1] + car[1] < xn:
            sum += (yn + store[i][1] + car[1])
        else:
            sum += (yn + 2 * xn - store[i][1] - car[1])
    elif store[i][0] + car[0] == 7:
        if store[i][1] + car[1] < yn:
            sum += (xn + store[i][1] + car[1])
        else:
            sum += (xn + 2 * yn - store[i][1] - car[1])
    else:
        if store[i][0] == 1:
            if car[0] == 3:
                sum += (store[i][1] + car[1])
            elif car[0] == 4:
                sum += (xn - store[i][1] + car[1])
        elif store[i][0] == 2:
            if car[0] == 3:
                sum += (store[i][1] + yn - car[1])
            elif car[0] == 4:
                sum += (xn - store[i][1] + yn - car[1])
        elif store[i][0] == 3:
            if car[0] == 1:
                sum += (store[i][1] + car[1])
            elif car[0] == 2:
                sum += (yn - store[i][1] + car[1])
        elif store[i][0] == 4:
            if car[0] == 1:
                sum += (store[i][1] + xn - car[1])
            elif car[0] == 2:
                sum += (yn - store[i][1] + xn - car[1])

print(sum)