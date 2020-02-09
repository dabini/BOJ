stairs_num = int(input())
stair_lst = []
for n in range(stairs_num):
    stair = int(input())
    stair_lst += [stair]
howmany = len(stair_lst)
ans = 0
def Getsome(here):
    global ans, howmany

    if here > howmany:
        return
    elif here == howmany:
        return
    else:
        ans += stair[here]
        return Getsome(here+1)
        return Getsome(here+2)
Getsome(0)
print(ans)