def switch(lst, i):
    if lst[i] == 1:
        lst[i] -= 1
    elif lst[i] == 0:
        lst[i] += 1
    return lst

num = int(input()) #스위치 개수
sw_lst = list(map(int, input().split())) #스위치 상태 켜져있으면 1 꺼져있으면 0
stu_num = int(input()) #학생수 남학생1 여학생2
for stu in range(stu_num):
    s, n = map(int, input().split())  #s 성별 n 비교할 수

    if s == 1:
        for i in range(num):
            if (i+1) % n == 0:
                switch(sw_lst, i)

    elif s == 2:
        k = 0
        for i in range(num):
            if i == n-1:
                while i-1-k >= 0 and i+1+k <= num-1:
                    if sw_lst[(i-1)-k] != sw_lst[i+1+k]:
                        break
                    else:
                        switch(sw_lst, i-1-k)
                        switch(sw_lst, i+1+k)
                    k += 1
                switch(sw_lst, i)
                break
for i in range(0, num, 20):
    print(*sw_lst[i:i+20])